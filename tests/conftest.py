#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
conftest.py for pycr.
"""

import pytest
import pandas as pd
import os
from pycr.pcrparser import PcrParser


cur_path = f"{os.path.dirname(__file__)}/pycr/data"


@pytest.fixture(scope = "session")
def df_input():
    df_input = pd.read_csv(f"{cur_path}/test_data.csv")
    return df_input

def df_expected():
    df_expected = pd.read_csv(f"{cur_path}/test_expected.csv")
    return df_expected

@pytest.fixture(scope = "session")
def rna_parser():

    rna_parser = PcrParser(
    file_path = "./data/raw_data.csv",
    control = "control",
    normalizer = "rpl19",
    target = "egf1r")

    return rna_parser
