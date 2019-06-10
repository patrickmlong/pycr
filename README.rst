====
pycr
====


A package to automate quantitative PCR analysis. 

This package uses argparse with the following entry points::

    $ runner.py -h

    positional arguments:
      file_path         The path to your RNA CT data csv file
      file_name         Your raw rna ct data csv file for relative expression
                        analysis
      pos_group         Your positive experimental group
      neg_group         Your negative experimental group
      output_file_name  Your RNA CT data csv input


Note
====

This project has been set up using PyScaffold 3.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
