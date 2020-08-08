[![Documentation Status](https://readthedocs.org/projects/docs/badge/?version=latest)](https://pycr.readthedocs.io/en/latest/) Check out the [pycr documentation on ReadTheDocs](https://pycr.readthedocs.io/en/latest/). 


pycr
====
A small utility package to automate [relative quantification of mRNA](https://en.wikipedia.org/wiki/Real-time_polymerase_chain_reaction) from thermocycler ct data. 
Currently assumes perfect amplification efficiency and unpaired samples.

<b>Installation</b>

    $ python -m pip install git+https://github.com/pkmklong/pycr.git

<b>Command line</b>

    $ pycr -h
    usage: pycr [-h] file_path experimental control

    positional arguments:
      file_path     The path to a ct data (csv) for relative RNA quantification
      experimental  The name of your experimental group
      control       The name of your control group

    optional arguments:
      -h, --help    show this help message and exit
      

<b>Input data dictionary</b>
```
{column name:     type      description}
group:            str       Name of experimental and control groups. Assumes bivariate analysis.
target:           float     ct values of target transcript.
normalizer:       float     ct values of housekeeping transcript.
```

<b>Fold expression</b>

<img src="https://github.com/pkmklong/pycr/blob/master/images/ddct_bk.png" height="100"  class="center" title="delta delta CT">


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
