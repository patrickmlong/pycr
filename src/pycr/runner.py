import argparse
from pycr import PcrParser 


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("file_path", 
	help = "the path to your raw rna CT data csv file for delta CT RNA level analysis",
	type = str)
	
	parser.add_argument("input_file_name", 
	help = "your raw rna ct data csv file for delta CT RNA level analysis",
	type = str)
	
	parser.add_argument("experimental",
	help = "The name of your experimental group",
	type = str)
	
	parser.add_argument("control",
	help = "The name of your control group",
	type = str)
	
	parser.add_argument("output_file_name", 
	help = "csv file name for RNA analysis results",
	type = str)
	
    # Run pycr using arguments
	args = parser.parse_args()
	
	rna_parser = PcrParser(args.file_path,args.pos_group, args.neg_group)
						   
	input_table = rna_parser.input_table(args.file_name)
	
	input_table = rna_parser.format_table()
	
	rna_parser.save_table_to_csv(args.output_file_name)
	
	
if __name__=='__main__':
	main()
