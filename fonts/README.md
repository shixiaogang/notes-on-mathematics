# 项目字体

本目录保存书籍当前使用的字体原始文件。克隆仓库后即可构建，无需把字体安装到操作系统中。字体保留原始字形，不转换或裁剪。图内排字另收录下表中的 Normal 与数学字体。

## 字体清单与来源

| 字体 | 收录字形与版本 | 上游来源 | 许可证 |
| --- | --- | --- | --- |
| Source Han Serif CN | Regular、Bold；1.000 | [思源宋体](https://github.com/adobe-fonts/source-han-serif) | [OFL](licenses/SourceHanSerif-OFL.txt) |
| Source Han Sans SC | Regular、Bold；2.004；图内 Normal 2.005 | [思源黑体](https://github.com/adobe-fonts/source-han-sans) | [OFL](licenses/SourceHanSans-OFL.txt) |
| LXGW WenKai / Mono | WenKai Regular、Medium，Mono Regular；1.522 | [霞鹜文楷](https://github.com/lxgw/LxgwWenKai) | [OFL](licenses/LXGWWenKai-OFL.txt) |
| STIX Two Text | Regular、Bold、Italic、BoldItalic；2.12 b168 | [STIX Fonts](https://github.com/stipub/stixfonts) | [OFL](licenses/STIX-OFL.txt) |
| Source Sans 3 | Regular、Semibold 及对应斜体；3.052 | [Source Sans](https://github.com/adobe-fonts/source-sans) | [OFL](licenses/SourceSans3-OFL.txt) |
| Source Code Pro | Regular、Semibold 及对应斜体；直立体 2.042，斜体 1.062 | [Source Code Pro](https://github.com/adobe-fonts/source-code-pro) | [OFL](licenses/SourceCodePro-OFL.txt) |
| Fira Math | Regular；0.3.4；图内英文、数字和数学 | [Fira Math](https://github.com/firamath/firamath) | [OFL](licenses/FiraMath-font-license.txt) |
| STIX Two Math | Regular；2.12 b168；仅补图内 Fira Math 缺失的数学字形 | [STIX Fonts](https://github.com/stipub/stixfonts) | [OFL](licenses/STIX-OFL.txt) |
| STIX2 Type 1 | TeX Live 2026 的 `stix2-type1` 字体资源，基于 STIX 2.0.0 | [STIX Fonts](https://github.com/stipub/stixfonts) | [OFL](licenses/STIX-OFL.txt) |

原书中文字体从原构建字体逐字节复制；新增思源黑体 Normal 与 Fira Math 来自本轮绘图封存字库，版本见上表。STIX Two Math 从 TeX Live 2026 复制。各字体保留内嵌的原始版本和版权信息；`licenses/` 中保存上游许可证。字体继续适用各自的 SIL Open Font License 1.1，不改用仓库根目录的 Apache 2.0 许可证。

## 加载方式

- `tex/styles/fonts.tex` 通过 `Path=fonts/` 加载本目录的 19 个 OpenType / TrueType 字体文件。
- `stix2-type1/` 保留完整的 Type 1 字体、度量、编码和映射资源，避免只收录当前几页用到的数学字形。`.latexmkrc` 设置本地优先的搜索路径，并为 PDF 转换器指定字体映射。
- `stix2` 宏包及其 LaTeX 字族定义仍由 TeX Live 提供；本目录不替代 TeX Live 安装。
- `build.sh` 在编译前检查必需字体；`clean` 只清理构建产物，不删除本目录。

## 完整性与更新

`SHA256SUMS` 记录字体二进制、度量、编码和映射文件的 SHA-256，路径相对仓库根目录。在根目录检查：

```sh
shasum -a 256 -c fonts/SHA256SUMS
```

更新字体时，应同时更新版本说明、对应许可证和校验清单，并执行干净构建及 PDF 检查。不要只更换某个字重而留下不配套的文件，也不要把系统字体链接提交到仓库。
