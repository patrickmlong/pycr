import pytest
from pycr.pcrparser import PcrParser
from pandas._testing import assert_frame_equal



# @pytest.mark.skip(reason="not yet written")
def test_check_columns():
    p = PcrParser.__new__(PcrParser)
    p.normalizer = "rpl19"
    p.target = "egf1r"
    df = pd.DataFrame(columns=["group", "rpl19", "not_expected"])
    with pytest.raises(KeyError):
        result = p.check_columns(df)


def test_calculate_ddct(rna_parser, df_input, df_expected):
    """test final results of format table yield expected"""

    df_result = rna_parser.calculate_ddct(df_input)
    assert_frame_equal(df_result, df_expected)
