[![Documentation Status](https://readthedocs.org/projects/docs/badge/?version=latest)](https://pycr.readthedocs.io/en/latest/) Check out the [pycr documentation on ReadTheDocs](https://pycr.readthedocs.io/en/latest/). 


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
"group":                            str     Names of comparison groups.
user defined target column:         float   ct values of target transcript.
user defined normalizing column:    float   ct values of normalizing reference transcript.
```

<b>Fold change</b>

<img src="https://github.com/pkmklong/pycr/blob/master/images/ddct.svg" height="250"  class="center" title="delta delta CT">


<b>Demo</b>

    $ pycr  ./data/demo_data_extended.csv control rpl19 egf1r
<br>    

    INFO:pycr:Loading table: ./data/demo_data_extended.csv
    INFO:pycr:Formatting table
    INFO:pycr:Saving output table: data/demo_data_extended_processed.csv
    INFO:pycr:Saving output figure: data/demo_data_extended_processed.png

<b>Tabular output</b>
|    | group   |   rpl19 |   egf1r |   delta_ct |   delta_delta_ct |   fold_change |
|---:|:--------|--------:|--------:|-----------:|-----------------:|--------------:|
|  3 | control | 17.7    | 25.4    |    7.7     |         -0.8665  |      1.82323  |
|  8 | control | 16.9    | 26.316  |    9.416   |          0.8495  |      0.554977 |
|  7 | control | 17.5    | 26.112  |    8.612   |          0.0455  |      0.968954 |
| 11 | trt_a   | 17.3    | 25.398  |    8.098   |         -0.4685  |      1.38367  |
| 15 | trt_a   | 17.3    | 24.9    |    7.6     |         -0.9665  |      1.95409  |
| 18 | trt_b   | 17.9895 | 25.9498 |    7.96032 |         -0.60618 |      1.52222  |
| 23 | trt_b   | 17.3865 | 25.647  |    8.2605  |         -0.306   |      1.23628  |
| 19 | trt_b   | 17.3865 | 26.1599 |    8.77344 |          0.20694 |      0.866373 |
| 24 | trt_b   | 17.3865 | 25.7397 |    8.3532  |         -0.2133  |      1.15934  |
| 25 | trt_b   | 17.487  | 25.5296 |    8.04258 |         -0.52392 |      1.43786  |
...

<b>Visualization</b>

<img src="https://github.com/pkmklong/pycr/blob/master/images/demo_data_extended_processed.png" height="400"  class="center" title="Demo visualization">


Note
====

This project has been set up using PyScaffold 3.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
