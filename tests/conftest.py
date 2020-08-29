#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
conftest.py for pycr.
"""

import pytest
from pycr.pcrparser import PcrParser

@pytest.fixture(scope = "session")
def rna_parser():

    rna_parser = PcrParser(
    file_path = "./data/raw_data.csv",
    control = "control",
    normalizer = "rpl19",
    target = "egf1r")

    return rna_parser
