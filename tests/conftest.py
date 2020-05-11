#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Dummy conftest.py for pycr.

    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    https://pytest.org/latest/plugins.html
"""

import pytest


@pytest.fixture(scope = "session")
def rna_parser():

    rna_parser = PcrParser(
    file_path = "/data/raw_data.csv",
    experimental = "plus_treatment",
    control = "without_treatment")

    return rna_parser
