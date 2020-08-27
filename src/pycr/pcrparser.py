import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger("pycr")

class PcrParser(object):
    """
    The PcrParser class creates a pipeline to automate  
    the analysis of RNA levels detected by RT-PCR.
    RNA expression is calculated using the delta Ct method.  
    """

    def __init__(self, file_path: str, control: str, normalizer: str, target: str):
        self.file_path = file_path
        self.control = control
        self.normalizer = normalizer
        self.target = target


    def make_output_path(self) -> str:
        """Create output path results"""
        
        output_path = f"{Path(self.file_path).parents[0]}" \
        f"/{Path(self.file_path).stem}_processed"
        
        return output_path

      
    def load_table(self) -> pd.DataFrame:
        """"Load input table and format appropriate headers"""
        
        logger.info(f"Loading table: {self.file_path}")
        df = pd.read_csv(Path(self.file_path))
        
        try:
            df = df.loc[:,["group", self.normalizer, self.target]]
        except AttributeError:
            logger.info("Columns: group, target, an/or normalizer not in table " \
                  f"columns:{df.columns}")
            #import pdb; pdb.set_trace()

        return df


    def format_table(self, df: pd.DataFrame) -> pd.DataFrame:
        """Calculate relative mRNA levels using delta delta ct"""
        
        logger.info("Formatting table...")
        
        df["delta_ct"] = \
        df[self.target] - df[self.normalizer]

        avg_delta_ct_control = \
        df[df.group == self.control].delta_ct.mean()
        
        df["delta_delta_ct"] = \
        df.delta_ct - avg_delta_ct_control

        df["fold_change"] = \
        2 ** (-df.delta_delta_ct)

        return df

      
    def save_table_to_csv(self, df: pd.DataFrame, output_path: str) -> None:
        """Save output file suffixed with "_processed.csv"""
        
        output = output_path + ".csv"
        logger.info(f"Saving output table: {output}" \

        f"\n {df.sample(10).sort_values(by ='group').to_markdown()} \n ....")
        df.to_csv(output, index = False)


    def visualize_rt(self, df: pd.DataFrame, output_path: str) -> None:
        """Visualization fold change in target gene expression"""

        output = output_path +  ".png"
        logger.info(f"Saving output figure: {output}")

        f, axes = plt.subplots(1, 2)
        sns.set(style = "white")

        sns.boxplot(x = "group",
              y =  "fold_change",
              data = df,
              ax=axes[0], width=.5, palette="GnBu")
        sns.boxplot(x = "group",
              y =  self.normalizer,
              data = df,
              ax=axes[1], width=.5, palette="GnBu")

        sns.swarmplot(x = "group",
              y =  "fold_change",
              data = df,
              ax=axes[0], color=".25")
        sns.swarmplot(x = "group",
              y =  self.normalizer,
              data = df,
           ax=axes[1], color=".25")

        plt.tight_layout()
        sns.despine(left=True)
        axes[0].set_ylabel(f'{self.target} fold change')
        axes[1].set_ylabel(f'{self.normalizer} ct values')
        axes[0].tick_params(labelrotation=45)
        axes[1].tick_params(labelrotation=45)
        f.savefig(output, dpi=300, bbox_inches="tight")
