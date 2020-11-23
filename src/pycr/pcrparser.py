import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import logging
from typing import IO

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger("pycr")


class PcrParser:
    """
    The PcrParser class creates a pipeline to automate
    the analysis of RNA levels detected by RT-PCR.
    RNA expression is calculated using the delta Ct method.
    """

    def __init__(
        self, file_path: str, control: str, normalizer: str, target: str
    ) -> None:
        self.file_path = file_path
        self.control = control
        self.normalizer = normalizer
        self.target = target

    def make_output_path(self) -> str:
        """Create output path results

        Returns:
            str: save path for ddct analysis outputs
        """

        output_path = (
            f"{Path(self.file_path).parents[0]}"
            f"/{Path(self.file_path).stem}_processed"
        )

        return output_path

    def load_table(self) -> pd.DataFrame:
        """ "Load input table

        Returns:
            pd.DataFrame: raw ct table for analysis
        """

        LOGGER.info(f" Loading table: {self.file_path}")
        df = pd.read_csv(Path(self.file_path))

        return df

    def check_columns(self, df: pd.DataFrame) -> None:
        """ "Check input table columns

        Args:
            df (pd.DataFrame): Raw ct values input table
        
        Returns:
            None
            
        Raises:
            KeyError: Error occurs if columns are not found
        """

        try:
            df = df.loc[:, ["group", self.normalizer, self.target]]
        except KeyError:
            LOGGER.info(
                f" KeyError. Columns: group, target, an/or normalizer not in table "
                f"columns:{df.columns}"
            )
            # import pdb; pdb.set_trace()
            raise

    def calculate_ddct(self, df: pd.DataFrame) -> pd.DataFrame:
        """Calculate relative mRNA levels using delta delta ct

        Args:
            df (pd.DataFrame): Raw ct values input dataframe
        
        Returns:  
            pd.DataFrame: delta delta ct table with fold change(s) in target gene expression
        """

        LOGGER.info(" Calculated delta delta ct...")

        df["delta_ct"] = df[self.target] - df[self.normalizer]

        avg_delta_ct_control = df[df.group == self.control].delta_ct.mean()

        df["delta_delta_ct"] = df.delta_ct - avg_delta_ct_control

        df["fold_change"] = 2 ** (-df.delta_delta_ct)

        return df

    def calculate_percent_expression(self, df: pd.DataFrame) -> pd.DataFrame:
        
        LOGGER.info(" Calculated percent change...")
        #df["delta_ct"] = df[self.target] - df[self.normalizer]
        df["expression"] = -(2 ** (-df.delta_delta_ct))
        df["average_expression"] = df[df.group == self.control].expression.mean()
        df["percent_expression"] = (df.expression / df.average_expression) * 100

        LOGGER.info(df.columns)
        
        return df
    

    @staticmethod
    def save_table_to_csv(df: pd.DataFrame, output_path: str) -> IO:
        """Save output file suffixed with "_processed.csv

        Args:
            df (pd.DataFrame): Raw ct values dataframe

        Returns:
            None

        IO:
            csv: delta delta ct table with fold change(s) in target gene expression
        """

        output = output_path + ".csv"
        LOGGER.info(
            f" Saving output table: {output}"
            f"\n {df.sample(10).sort_values(by ='group').to_markdown()} \n ...."
        )
        df.to_csv(output, index=False)

    def visualize_rt(self, df: pd.DataFrame, output_path: str) -> IO:
        """Visualization fold change in target gene expression

        Args:
            df (pd.DataFrame): Raw ct values dataframe
            output_path (str): file save path

        Returns:
            None

        IO:
            png: matplotlib.figure of relative target gene expression expressed as fold change
        """

        output = output_path + ".png"
        LOGGER.info(f" Saving output figure: {output}")

        figure, axes = plt.subplots(2, 2)
        sns.set(style="white")

        palette = "GnBu"
        width = 0.5
        color = ".25"
        labelrotation = 45
        
        sns.boxplot(
            x="group", y="fold_change", data=df, ax=axes[0,0], width=width, palette=palette
        )
        sns.swarmplot(x="group", y="fold_change", data=df, ax=axes[0], color=color)
        axes[0,0].set_ylabel(f"{self.target} Fold Change")
        axes[0,0].tick_params(labelrotation=labelrotation)  
        
        sns.boxplot(
            x="group", y="percent_expression", data=df, ax=axes[0,1], width=width, palette=palette
        )
        sns.swarmplot(x="group", y="percent_expression", data=df, ax=axes[0,1], color=color)
        axes[0,1].set_ylabel(f"{self.target} Percent Expression")
        axes[0,1].tick_params(labelrotation=labelrotation)  
        
        sns.boxplot(
            x="group", y=self.target, data=df, ax=axes[1,0], width=width, palette=palette
        )
        sns.swarmplot(x="group", y=self.target, data=df, ax=axes[1,0], color=color)
        axes[1,0].set_ylabel(f"{self.target} ct values")
        axes[1,0].tick_params(labelrotation=labelrotation)
        
        sns.boxplot(
            x="group", y=self.normalizer, data=df, ax=axes[1,1], width=width, palette=palette
        )
        sns.swarmplot(x="group", y=self.normalizer, data=df, ax=axes[1,1], color=color)
        axes[1,1].set_ylabel(f"{self.normalizer} ct values")
        axes[1,1].tick_params(labelrotation=labelrotation)
        
        plt.tight_layout()
        sns.despine(left=True)

        figure.savefig(output, dpi=300, bbox_inches="tight")

