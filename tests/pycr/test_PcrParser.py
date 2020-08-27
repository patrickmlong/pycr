import pytest
from pycr.pcrparser import PcrParser
import pandas as pd
from pandas._testing import assert_frame_equal
import os

# import test data
cur_path = f"{os.path.dirname(__file__)}/data/"
df_input = pd.read_csv(f"{cur_path}test_data.csv")
df_expected = pd.read_csv(f"{cur_path}test_expected.csv")


@pytest.mark.skip(reason="not yet written")
def test_load_table():
    pass


def test_format_table():
    """test final results of format table yield expected"""

    p = PcrParser(None, "control", "rpl19", "egf1r")
    df_result = p.format_table(df_input)
    assert_frame_equal(df_result, df_expected)
