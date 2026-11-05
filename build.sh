#!/usr/bin/env bash

set -euo pipefail

project_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$project_root"

usage() {
  printf '用法: %s [build|volume <slug>|volumes|all|check-target|watch <slug>|release <slug>|clean]\n' "${0##*/}"
  printf '  build          仅编译输入变化、缺失或损坏的卷（默认）\n'
  printf '  volume <slug>  只编译指定单卷\n'
  printf '  volumes/all    首次构建或全书变更时编译目录登记的各卷\n'
  printf '  check-target   检查各卷成品和构建记录\n'
  printf '  watch <slug>   监听指定卷，成功后更新该卷成品和记录\n'
  printf '  release <slug> 以最高无损压缩等级编译指定卷\n'
  printf '  clean          清除本工作区的构建缓存和产物\n'
  python3 scripts/book_catalog.py slugs
}

require_latexmk() {
  if ! command -v latexmk >/dev/null 2>&1; then
    printf '错误：未找到 latexmk，请先安装包含 XeLaTeX 的 TeX Live。\n' >&2
    exit 1
  fi
}

# 字体随仓库分发；不搜索系统字体，也不复用旧的构建期链接。
prepare_fonts() {
  local font_file
  local required_fonts=(
    FiraMath-Regular.otf
    STIXTwoMath-Regular.otf
    SourceHanSansSC-Normal.otf
    LXGWWenKai-Medium.ttf
    LXGWWenKai-Regular.ttf
    LXGWWenKaiMono-Regular.ttf
    STIXTwoText-Bold.otf
    STIXTwoText-BoldItalic.otf
    STIXTwoText-Italic.otf
    STIXTwoText-Regular.otf
    SourceCodePro-Regular.otf
    SourceCodePro-RegularIt.otf
    SourceCodePro-Semibold.otf
    SourceCodePro-SemiboldIt.otf
    SourceHanSansSC-Bold.otf
    SourceHanSansSC-Regular.otf
    SourceHanSerifCN-Bold.otf
    SourceHanSerifCN-Regular.otf
    SourceSans3-Regular.otf
    SourceSans3-RegularIt.otf
    SourceSans3-Semibold.otf
    SourceSans3-SemiboldIt.otf
    stix2-type1/type1/STIX2Math.pfb
    stix2-type1/map/stix2.map
  )
  for font_file in "${required_fonts[@]}"; do
    if [[ ! -f "fonts/$font_file" ]]; then
      printf '错误：缺少仓库字体 fonts/%s，请恢复完整的 fonts/ 目录。\n' "$font_file" >&2
      return 1
    fi
  done
}

build_volume() {
  local slug="$1"
  local entry
  entry="$(python3 -c 'import sys; from scripts.book_catalog import volumes; v=next((v for v in volumes() if v["slug"]==sys.argv[1]), None); sys.exit("未知卷名："+sys.argv[1]) if v is None else print(v["entry"]+" "+v["pdf"])' "$slug")"
  local source="${entry%% *}"
  local output="target/${entry#* }"

  require_latexmk
  prepare_fonts
  python3 scripts/book_catalog.py references "$slug"
  local snapshot
  snapshot="$(mktemp "${TMPDIR:-/tmp}/book-inputs.XXXXXX")"
  python3 scripts/check_target_pdfs.py snapshot > "$snapshot"
  local compression="${BOOK_PDF_COMPRESSION:-1}"
  local previous_compression=""
  local job_name="$slug"
  local cached_pdf="build/$job_name.pdf"
  local compression_cache="build/.pdf-compression-$job_name"
  local latexmk_options=(-interaction=nonstopmode -halt-on-error -file-line-error)
  case "$compression" in
    [0-9]) ;;
    *) printf '错误：BOOK_PDF_COMPRESSION 必须为 0 到 9 的整数。\n' >&2; return 1 ;;
  esac
  if [[ -f "$compression_cache" ]]; then
    previous_compression="$(cat "$compression_cache")"
  fi
  # latexmk 不一定因 PDF 转换命令变化而重建；显式处理模式切换。
  if [[ -f "$cached_pdf" && "$previous_compression" != "$compression" ]]; then
    latexmk_options+=(-g)
  fi
  latexmk \
    "${latexmk_options[@]}" \
    -jobname="$job_name" \
    "$source"
  mkdir -p target
  cp "$cached_pdf" "$output.tmp"
  mv "$output.tmp" "$output"
  printf '%s\n' "$compression" > "$compression_cache"
  python3 scripts/check_target_pdfs.py record --volume "$slug" --snapshot "$snapshot"
  rm -f "$snapshot"
}

build_volumes() {
  local slug
  while IFS= read -r slug; do
    [[ -n "$slug" ]] || continue
    build_volume "$slug"
  done < <(python3 scripts/book_catalog.py slugs)
}

clean_project() {
  rm -rf -- "$project_root/build" "$project_root/target"
}

case "${1:-build}" in
  build)
    affected="$(python3 scripts/check_target_pdfs.py affected)"
    if [[ -z "$affected" ]]; then
      printf '各卷输入与成品一致，无需重新编译。\n'
    else
      while IFS= read -r slug; do
        build_volume "$slug"
      done <<< "$affected"
    fi
    python3 scripts/check_target_pdfs.py check
    ;;
  volume)
    if [[ -z "${2:-}" ]]; then
      printf '错误：volume 缺少卷名，使用 --help 查看可用卷名。\n' >&2
      exit 2
    fi
    build_volume "$2"
    ;;
  volumes)
    build_volumes
    ;;
  all)
    build_volumes
    python3 -c 'from pathlib import Path; from scripts.book_catalog import volumes; expected={v["pdf"] for v in volumes()}; [p.unlink() for p in Path("target").glob("*.pdf") if p.name not in expected]'
    python3 scripts/check_target_pdfs.py check
    ;;
  check-target)
    python3 scripts/check_target_pdfs.py check
    ;;
  watch)
    [[ -n "${2:-}" ]] || { usage >&2; exit 2; }
    build_volume "$2"
    export BOOK_WATCH_SLUG="$2"
    latexmk -interaction=nonstopmode -halt-on-error -file-line-error \
      -jobname="$2" -pvc -view=none "tex/$2/main.tex"
    ;;
  release)
    export BOOK_PDF_COMPRESSION=9
    [[ -n "${2:-}" ]] || { usage >&2; exit 2; }
    build_volume "$2"
    ;;
  clean)
    clean_project
    ;;
  -h|--help|help)
    usage
    ;;
  *)
    usage >&2
    exit 2
    ;;
esac
