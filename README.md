pycr
====
A small utility package to automate quantification of relative mRNA expression.

<img src="https://github.com/pkmklong/pycr/blob/master/images/Qpcr-cycling.png" height="200"  class="center" title="RNA amplification">

<b>Installation</b>

    $ git clone https://github.com/pkmklong/pycr.git pycr
    $ cd pycr
    $ pip install .


<b>Command line</b>

    $ pycr -h
    usage: pycr [-h] file_path experimental control

    positional arguments:
      file_path     The path to rna cycle threshold data (csv) for delta ct relative RNA quantification
      experimental  The name of your experimental group
      control       The name of your control group

    optional arguments:
      -h, --help    show this help message and exit
      

<b>Demo</b>

    $ pycr  ./data/demo_data.csv treatment no_treatment
<br>    

    INFO:pycr:Loading table: ./data/demo_data.csv
    INFO:pycr:Formatting table
    INFO:pycr:Saving output table: data/demo_data_processed.csv
    INFO:pycr:Saving output figure: data/demo_data_processed.png

<b>Demo visualization</b>

<img src="https://github.com/pkmklong/pycr/blob/master/images/demo_data_processed.png" height="300"  class="center" title="Demo visualization">

Note
====

This project has been set up using PyScaffold 3.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
