====
pycr
====


A package to automate quantitative PCR analysis. 
This package uses argparse and has the following entry points::

    $ runner.py -h

    positional arguments
    -file_path         the path to your raw rna ct data csv file for relative
                       expression analysis
    -file_name         The name of your raw rna ct data csv file for relative
                        expression analysis
    -pos_group         The name of your positive experimental group
    -neg_group         The name of your negative experimental group
    -output_file_name  The name of your RNA CT data csv input

    optional arguments
    -h, --help        show this help message and exit


Note
====

This project has been set up using PyScaffold 3.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
