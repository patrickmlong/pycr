#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
conftest.py for pycr.
"""

import pytest
from pycr.pcrparser import PcrParser


cur_path = f"{os.path.dirname(__file__)}/pycr/data"


@pytest.fixture(scope = "session")
def df_input():
    return df_input = pd.read_csv(f"{cur_path}/test_data.csv")

def df_expected():
    return df_expected = pd.read_csv(f"{cur_path}/test_expected.csv")

@pytest.fixture(scope = "session")
def rna_parser():

    rna_parser = PcrParser(
    file_path = "./data/raw_data.csv",
    control = "control",
    normalizer = "rpl19",
    target = "egf1r")

    return rna_parser
