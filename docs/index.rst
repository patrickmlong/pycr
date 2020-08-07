Pycr documentation
=====================================

Installation::

    $ git clone https://github.com/pkmklong/pycr.git pycr
    $ cd pycr
    $ pip install .


Running pycr::

    $ pycr -h

        usage: pycr [-h] file_path experimental control

        positional arguments:
            file_path     The path to rna cycle threshold tabular data (csv) for delta ct relative RNA quantification
            experimental  The name of your experimental group
            control       The name of your control group
            
        optional arguments:
            -h, --help    show this help message and exit

Demo::

    $ pycr  ./data/demo_data.csv treatment no_treatment

    INFO:pycr:Loading table: ./data/demo_data.csv
    INFO:pycr:Formatting table
    INFO:pycr:Saving output table: data/demo_data_processed.csv
    INFO:pycr:Saving output figure: data/demo_data_processed.png

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   license


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
