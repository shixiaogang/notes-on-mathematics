$pdf_mode = 5;
$xelatex = 'xelatex %O %S';
$out_dir = 'build';
# macOS 上优先使用可执行的 Homebrew Biber；其他环境继续从 PATH 查找。
$biber = -x '/opt/homebrew/bin/biber'
    ? '/opt/homebrew/bin/biber %O %S'
    : 'biber %O %S';
$makeindex = 'texindy -L general -C utf8 -M ../tex/styles/book-index.xdy %O -o %D %S';

# 最高压缩等级会反复压缩大幅 PNG 和嵌入字体。日常使用快速无损压缩，
# release 模式通过环境变量恢复等级 9；不降低分辨率或更换字体。
my $book_compression = $ENV{'BOOK_PDF_COMPRESSION'} // '1';
die "BOOK_PDF_COMPRESSION must be an integer from 0 to 9\n"
    unless $book_compression =~ /\A[0-9]\z/;
$xdvipdfmx = "xdvipdfmx -f fonts/stix2-type1/map/stix2.map -E -z $book_compression %O -o %D %S";

# 始终优先使用 tex/styles/ 中固定版本的 Tufte-LaTeX。
$ENV{'TEXINPUTS'} = './tex//:' . ($ENV{'TEXINPUTS'} // '');

# STIX2 Type 1 字体、度量与编码固定在仓库；保留末尾默认搜索路径供其他宏包使用。
$ENV{'T1FONTS'} = './fonts/stix2-type1/type1//:' . ($ENV{'T1FONTS'} // '');
$ENV{'TFMFONTS'} = './fonts/stix2-type1/tfm//:' . ($ENV{'TFMFONTS'} // '');
$ENV{'ENCFONTS'} = './fonts/stix2-type1/enc//:' . ($ENV{'ENCFONTS'} // '');

# watch refreshes source-derived locations before compiling, then publishes
# only this volume after latexmk's successful bibliography/index cycle.
if (defined $ENV{'BOOK_WATCH_SLUG'}) {
    my $slug = $ENV{'BOOK_WATCH_SLUG'};
    die "Invalid volume slug\n" unless $slug =~ /\A[0-9]{2}-[a-z-]+\z/;
    $xelatex = "python3 scripts/book_catalog.py references $slug && python3 scripts/check_target_pdfs.py snapshot > build/$slug-inputs.json && xelatex %O %S";
    $success_cmd = "python3 scripts/publish_volume.py $slug";
}

1;
