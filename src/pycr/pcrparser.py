"""
The PcrParser class creates a pipeline to automate the analysis of RNA levels detected by RT-PCR.
RNA expression is calculated using the delta Ct method.
"""
    
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import logging
from typing import IO

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger("pycr")


class PcrParser:

    def __init__(
        self, control: str, normalizer: str, target: str) -> None:
        self.control = control
        self.normalizer = normalizer
        self.target = target

    def _check_columns(self, df: pd.DataFrame) -> None:
        """ "Check input table columns

        :param df: Raw ct values input table
        :type df: pd.DataFrame
        :return: Exception if columns are not present otherwise None
        :rtype: None
        """

        try:
            df = df.loc[:, ["group", self.normalizer, self.target]]
        except KeyError:
            LOGGER.info(
                " Columns: group, target, an/or normalizer not in table "
                f"columns:{df.columns}"
            )
            # import pdb; pdb.set_trace()
            raise

    def calculate_ddct(self, df: pd.DataFrame) -> pd.DataFrame:
        """Calculate relative mRNA levels using delta delta ct

        :param df: Raw ct values input dataframe
        :type df: pd.DataFrame
        :return:  delta delta ct table with fold change(s) in target gene expression
        :rtype: pd.DataFrame
        """

        _check_columns(df)
        
        LOGGER.info(" Calculated delta delta ct...")

        df["delta_ct"] = df[self.target] - df[self.normalizer]

        avg_delta_ct_control = df[df.group == self.control].delta_ct.mean()

        df["delta_delta_ct"] = df.delta_ct - avg_delta_ct_control

        df["fold_change"] = 2 ** (-df.delta_delta_ct)

        return df

    def visualize_rt(self, df: pd.DataFrame, output_path: str) -> IO:
        """Visualization fold change in target gene expression"""

        output = output_path + ".png"
        LOGGER.info(f" Saving output figure: {output}")

        figure, axes = plt.subplots(1, 2)
        sns.set(style="white")

        sns.boxplot(
            x="group", y="fold_change", data=df, ax=axes[0], width=0.5, palette="GnBu"
        )
        sns.boxplot(
            x="group", y=self.normalizer, data=df, ax=axes[1], width=0.5, palette="GnBu"
        )

        sns.swarmplot(x="group", y="fold_change", data=df, ax=axes[0], color=".25")
        sns.swarmplot(x="group", y=self.normalizer, data=df, ax=axes[1], color=".25")

        plt.tight_layout()
        sns.despine(left=True)
        axes[0].set_ylabel(f"{self.target} fold change")
        axes[1].set_ylabel(f"{self.normalizer} ct values")
        axes[0].tick_params(labelrotation=45)
        axes[1].tick_params(labelrotation=45)
        figure.savefig(output, dpi=300, bbox_inches="tight")
