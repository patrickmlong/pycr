====
pycr
====

A package to automate quantitative PCR analysis for delta CT mRNA quantification. 

image:: ./images/Qpcr-cycling.png

Installation::

    $ git clone https://github.com/patrickmlong/pycr.git pycr
    $ cd pycr
    $ pip install .


This package uses the pycr entry point with the following arguments::

    $ pycr -h
    usage: pycr [-h]
                file_path input_file_name experimental control output_file_name

    positional arguments:
      file_path         the path to your raw rna CT data csv file for delta CT RNA
                        level analysis
      input_file_name   your raw rna ct data csv file for delta CT RNA level
                        analysis
      experimental      The name of your experimental group
      control           The name of your control group
      output_file_name  csv file name for RNA analysis results


Note
====

This project has been set up using PyScaffold 3.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
