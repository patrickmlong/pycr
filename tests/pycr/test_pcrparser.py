import pytest
from pycr.pcrparser import PcrParser
import pandas as pd
from pandas._testing import assert_frame_equal
import os

## import test data
#cur_path = f"{os.path.dirname(__file__)}/data/"
#df_input = pd.read_csv(f"{cur_path}test_data.csv")
#df_expected = pd.read_csv(f"{cur_path}test_expected.csv")


# @pytest.mark.skip(reason="not yet written")
def test_check_columns():
    p = PcrParser.__new__(PcrParser)
    p.normalizer = "rpl19"
    p.target = "egf1r"
    df = pd.DataFrame(columns=["group", "rpl19", "not_expected"])
    with pytest.raises(KeyError):
        result = p.check_columns(df)


def test_calculate_ddct(rna_parser):
    """test final results of format table yield expected"""

    df_result = rna_parser.calculate_ddct(df_input)
    assert_frame_equal(df_result, df_expected)
