import pytest
from pycr.pcrparser.runner import main as cl
from pycr.pcrparser import PcrParser


def test_runner():
    p = PcrParser("expected_path", "expected_control", "expected_normalizer", "expected_target") 
    parser = cl.(["expected_path", "expected_control", "expected_normalizer", "expected_target"])
    self.assertTrue(parser.long)
