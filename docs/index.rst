Pycr documentation
=====================================
A small utility package to automate relative quantification of mRNA from thermocycler cycle threshold (ct) data. Takes as input raw ct values for target and reference genes from experiment and control conditions and returns as output the fold changes in gene expression using the |Dgr| |Dgr| ct method. 

Installation::

    $ python -m pip install git+https://github.com/pkmklong/pycr.git

Running pycr::

    $ pycr -h

        usage: pycr [-h] file_path control normalizer target

        positional arguments:
            file_path     The path to ct data (csv) for relative RNA quantification 
            control       The name of your control group
            normalizer    The name of your normalizing reference transcript
            target        The name of your target transcript
            
        optional arguments:
            -h, --help    show this help message and exit



Input data dictionary::

    {column:                            type    description}
    "group":                            str     Names of comparison groups.
    user defined normalizing column:    float   ct values of normalizing reference transcript.
    user defined target column:         float   ct values of target transcript.


Fold change:

.. image:: ../images/ddct.svg
  :width: 500
  :alt: delta delta CT 


Demo::

    $ pycr  ./data/demo_data_extended.csv control rpl19 egf1r

    INFO:pycr:Loading table: ./data/demo_data_extended.csv
    INFO:pycr:Formatting table
    INFO:pycr:Saving output table: data/demo_data_extended_processed.csv
    INFO:pycr:Saving output figure: data/demo_data_extended_processed.png


Outputs::

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


.. image:: ../images/demo_data_extended_processed.png
  :width: 500
  :alt: Demo visualization 


.. note::
    Currently assumes perfect amplification efficiency and unpaired samples.


.. include:: isogrk1.txt


.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   license


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
