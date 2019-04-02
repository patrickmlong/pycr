import pandas as pd
import os

class PcrParser(object):
    """
    The PcrParser class create an RT-PCR analysis
    pipeline to automate the analysis of relative mRNA levels.
    Expression is calculated using the delta Ct method.  
    """
    
    def __init__(self, file_path, pos_group, neg_group):
        self.file_path = file_path
        self.pos_group = pos_group
        self.neg_group = neg_group
        self.rt_table = pd.DataFrame()
        
    
    def input_table(self, file_name):
        self.rt_table = \
        os.path.join(os.path.normpath(self.file_path,
                                      elf.file_name))
        self.rt_table = \
        self.rt_table.loc[:,["sample", "Cq Mean"]]
        
      
    def format_table(self):
        pass
    
    def visualize_rt(self):
        pass
    
    def save_table_to_csv(self):
        pass
        
        
    