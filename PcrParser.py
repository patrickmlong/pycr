import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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
        	import pdb; pdb.set_trace()
        	
        try:
        	self.rt_table = \
        	self.rt_table.loc[:,["group", "target", "normalizer"]]
        	
        except:
              print("Columns: "group, target, an/or normalizer" not in table " \
               "columns: {}".format(self.rt_table.columns))
               import pdb; pdb.set_trace()
                  
      
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
    	(self.rt_table.expression / self.rt_table.average) *  100
    	 
    
    def visualize_rt(self):
    
    	sns.set(style = "whitegrid")
    	
    	sns.boxplot(x = "group", y =  "percent_average",
    	            data = self.rt_table)

    
    def save_table_to_csv(self, file_name):
    
        self.rt_table.to_csv(os.pathjoin(os. \
        path.normpath(self.file_path, file_name)), index = False)
        
        
    