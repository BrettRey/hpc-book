# Latexmk configuration for HPC Book
# Output all build artifacts to build/ directory

$out_dir = 'build';
$aux_dir = 'build';

# Use XeLaTeX
$pdf_mode = 5;  # xelatex -> xdvipdfmx
$xelatex = 'xelatex -interaction=nonstopmode %O %S';
$pdflatex = 'xelatex -interaction=nonstopmode %O %S';
$biber = 'biber %O %B';
$bibtex = 'biber %O %B';

# Run makeglossaries when needed
add_cus_dep('glo', 'gls', 0, 'run_makeglossaries');
add_cus_dep('acn', 'acr', 0, 'run_makeglossaries');

sub run_makeglossaries {
    my ($base_name, $path) = fileparse( $_[0] );
    pushd $path;
    my $return = system "makeglossaries", $base_name;
    popd;
    return $return;
}
