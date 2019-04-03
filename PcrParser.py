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
        try:
        	self.rt_table = \
        	os.path.join(os.path.normpath(self.file_path,
                                     file_name))
        except OSError:
        	print("File {} not found".format(file_name))
        	
        self.rt_table = \
        self.rt_table.loc[:,["sample", "Cq Mean"]]
        
      
    def format_table(self):
    	
    	self.rt_table["delta_ct"] = \
    	self.rt_table.target - self.rt_table.normalizer
    	
    	self.rt_table["expression"] = \
    	2 ** self.rt_table.delta_ct
    	
    	avg_negative = \
    	self.rt_table[self.rt_table.group == self.neg_group].mean()
    	avg_positive = \
    	self.rt_table[self.rt_table.group == self.positive_group].mean()
    	
    	self.rt_table["average"] = self.rt_table.apply(lambda x: \
    	 avg_negative if x == self.neg_group else avg_positive)
    	
    	self.rt_table["percent_average"] = \ 
    	(self.rt_table.expression * self.rt_table.average) *  100
    	 
    
    def visualize_rt(self):
        pass
    
    def save_table_to_csv(self):
        pass
        
        
    