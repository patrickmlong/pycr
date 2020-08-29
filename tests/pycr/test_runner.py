import pytest
from pycr.runner import parse_args


def test_runner():
    args = parse_args(["expected_path", "expected_control", "expected_normalizer", "expected_target"])
    assert args.file_path == "expected_path"
    assert args.control == "expected_control"
    assert args.normalizer == "expected_normalizer"
    assert args.target == "expected_target"
