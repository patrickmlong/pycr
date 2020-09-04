[![Documentation Status](https://readthedocs.org/projects/docs/badge/?version=latest)](https://pycr.readthedocs.io/en/latest/) Check out the [pycr documentation on ReadTheDocs](https://pycr.readthedocs.io/en/latest/).
<br> [![codecov](https://codecov.io/gh/pkmklong/pycr/branch/master/graph/badge.svg)](https://codecov.io/gh/pkmklong/pycr)
[![<ORG_NAME>](https://circleci.com/gh/pkmklong/pycr.svg?style=shield)](https://app.circleci.com/pipelines/github/pkmklong)

pycr
====
A small utility package to automate [relative quantification of mRNA](https://en.wikipedia.org/wiki/Real-time_polymerase_chain_reaction) from thermocycler ct data. 
Currently assumes perfect amplification efficiency and unpaired samples.

<b>Installation</b>

    $ python -m pip install git+https://github.com/pkmklong/pycr.git

<b>Command line</b>

    $ pycr -h
    usage: pycr [-h] file_path control normalizer target

    positional arguments:
        file_path     The path to ct data (csv) for relative RNA quantification
        control       The name of your control group
        normalizer    The name of your normalizing reference transcript
        target        The name of your target transcript

    optional arguments:
        -h, --help    show this help message and exit
        
        
<b>Input data dictionary</b>
```
{column:                            type    description}
"group":                            str     Names of comparison groups
user defined target column:         float   ct values of target transcript
user defined normalizing column:    float   ct values of normalizing reference transcript
```

<b>Fold change</b>

<img src="https://github.com/pkmklong/pycr/blob/master/images/ddct.svg" height="250"  class="center" title="delta delta CT">


<b>Demo</b>

    $ pycr  ./data/demo_data_extended.csv control rpl19 egf1r
<br>    

    INFO:pycr: Loading table: ./data/demo_data_extended.csv
    INFO:pycr: Calculating delta delta ct
    INFO:pycr: Saving output table: data/demo_data_extended_processed.csv
    |    | group   |   rpl19 |   egf1r |   delta_ct |   delta_delta_ct |   fold_change |
    |---:|:--------|--------:|--------:|-----------:|-----------------:|--------------:|
    |  1 | control | 16.9    | 25.8    |    8.9     |          0.3335  |      0.793609 |
    |  3 | control | 17.7    | 25.4    |    7.7     |         -0.8665  |      1.82323  |
    |  2 | control | 17.4    | 26      |    8.6     |          0.0335  |      0.977047 |
    |  6 | control | 17.7    | 25.908  |    8.208   |         -0.3585  |      1.28209  |
    |  4 | control | 17.2    | 25.45   |    8.25    |         -0.3165  |      1.24531  |
    | 17 | trt_a   | 17.4    | 24.786  |    7.386   |         -1.1805  |      2.26655  |
    | 20 | trt_b   | 17.487  | 25.029  |    7.542   |         -1.0245  |      2.03425  |
    | 23 | trt_b   | 17.3865 | 25.647  |    8.2605  |         -0.306   |      1.23628  |
    | 18 | trt_b   | 17.9895 | 25.9498 |    7.96032 |         -0.60618 |      1.52222  |
    | 22 | trt_b   | 17.9895 | 25.441  |    7.4515  |         -1.115   |      2.16595  | 
     ....
    INFO:pycr: Saving output figure: data/demo_data_extended_processed.png


<b>Visuals</b>

<img src="https://github.com/pkmklong/pycr/blob/master/images/demo_data_extended_processed.png" height="400"  class="center" title="Demo visualization">


Note
====

This project has been set up using PyScaffold 3.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
