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


    def __init__(self, file_path, experimental, control):
        self.file_path = file_path
        self.experimental = experimental
        self.control = control
        self.rt_table = pd.DataFrame()
        self.output_path = f"{Path(file_path).parents[0]}" \
        f"/{Path(file_path).stem}_processed"


    def input_table(self):
        """"Load input table and format appropriate headers"""
        logger.info(f"Loading table: {self.file_path}")
        try:
            self.rt_table = pd.read_csv(Path(self.file_path))
        except OSError:
            print(f"File {self.file_path} not found")
            import pdb; pdb.set_trace()
        	
        try:
            self.rt_table = self.rt_table.loc[:,["group", "target", "normalizer"]]
        except:
            logger.info("Columns: group, target, an/or normalizer not in table " \
                  f"columns:{self.rt_table.columns}")
            import pdb; pdb.set_trace()


    def format_table(self):
        """Calculate relative mRNA levels using delta delta ct"""
        
        logger.info("Formatting table")

        self.rt_table["delta_ct"] = \
        self.rt_table.target - self.rt_table.normalizer

        avg_delta_ct_control = \
        self.rt_table[self.rt_table.group == self.control].delta_ct.mean()
        
        self.rt_table["delta_delta_ct"] = \
        self.rt_table.delta_ct - avg_delta_ct_control

        self.rt_table["fold_change"] = \
        2 ** (-self.rt_table.delta_delta_ct)


    def save_table_to_csv(self):
        """Save output file suffixed with "_processed.csv"""
        
        output = self.output_path + ".csv"
        logger.info(f"Saving output table: {output}")
        self.rt_table.to_csv(output, index = False)


    def visualize_rt(self):
        """WIP add visualization method"""

        output = self.output_path +  ".png"
        logger.info(f"Saving output figure: {output}")
        sns.set(style = "white")
        sns.boxplot(x = "group",
                    y =  "fold_change",
                    data = self.rt_table)
        plt.savefig(output, dpi=300)
