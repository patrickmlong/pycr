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


    def __init__(self, file_path, control, normalizer, target):
        self.file_path = file_path
        self.control = control
        self.normalizer = normalizer
        self.target = target


    def make_output_path(self):
        """Create output path results"""
        output_path = f"{Path(self.file_path).parents[0]}" \
        f"/{Path(self.file_path).stem}_processed"
        return output_path

    def load_table(self):
        """"Load input table and format appropriate headers"""
        logger.info(f"Loading table: {self.file_path}")

        try:
            rt_table = pd.read_csv(Path(self.file_path))
        except OSError:
            print(f"File {self.file_path} not found")
            import pdb; pdb.set_trace()

        try:
            rt_table = rt_table.loc[:,["group", self.normalizer, self.target]]
        except:
            logger.info("Columns: group, target, an/or normalizer not in table " \
                  f"columns:{rt_table.columns}")
            import pdb; pdb.set_trace()

        return rt_table


    def format_table(self, rt_table):
        """Calculate relative mRNA levels using delta delta ct"""
        
        logger.info("Formatting table")
        
        rt_table["delta_ct"] = \
        rt_table[self.target] - rt_table[self.normalizer]

        avg_delta_ct_control = \
        rt_table[rt_table.group == self.control].delta_ct.mean()
        
        rt_table["delta_delta_ct"] = \
        rt_table.delta_ct - avg_delta_ct_control

        rt_table["fold_change"] = \
        2 ** (-rt_table.delta_delta_ct)

        return rt_table

    def save_table_to_csv(self, rt_table, output_path):
        """Save output file suffixed with "_processed.csv"""
        
        output = output_path + ".csv"
        logger.info(f"Saving output table: {output}" \
        f"\n {rt_table.sample(10).sort_values(by ='group').to_markdown()} \n ....")
        rt_table.to_csv(output, index = False)


    def visualize_rt(self, rt_table, output_path):
        """Visualization fold change in target gene expression"""

        output = output_path +  ".png"
        logger.info(f"Saving output figure: {output}")

        f, axes = plt.subplots(1, 2)
        sns.set(style = "white")

        sns.boxplot(x = "group",
              y =  "fold_change",
              data = rt_table,
              ax=axes[0], width=.5, palette="GnBu")
        sns.boxplot(x = "group",
              y =  self.normalizer,
              data = rt_table,
              ax=axes[1], width=.5, palette="GnBu")

        sns.swarmplot(x = "group",
              y =  "fold_change",
              data = rt_table,
              ax=axes[0], color=".25")
        sns.swarmplot(x = "group",
              y =  self.normalizer,
              data = rt_table,
           ax=axes[1], color=".25")

        plt.tight_layout()
        sns.despine(left=True)
        axes[0].set_ylabel(f'{self.target} fold change')
        axes[1].set_ylabel(f'{self.normalizer} ct values')
        axes[0].tick_params(labelrotation=45)
        axes[1].tick_params(labelrotation=45)
        f.savefig(output, dpi=300, bbox_inches="tight")
