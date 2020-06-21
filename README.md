pycr
====
A small utility package to automate quantification for mRNA. Fold mRNA expression is calculated via delta delta CT method.

<img src="https://github.com/patrickmlong/pycr/blob/master/images/Qpcr-cycling.png" height="200"  class="center" title="RNA amplification">

<b>Installation</b>

    $ git clone https://github.com/patrickmlong/pycr.git pycr
    $ cd pycr
    $ pip install .


<b>Command line entry point</b>

    $ pycr -h
    usage: pycr [-h] file_path experimental control

    positional arguments:
      file_path     The path to your raw rna CT data csv file for delta CT RNA
                level analysis
      experimental  The name of your experimental group
      control       The name of your control group

    optional arguments:
      -h, --help    show this help message and exit
      

<b>Demo</b>

    $ pycr  ./data/demo_data.csv no_treatment treatment
    
Note
====

This project has been set up using PyScaffold 3.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
