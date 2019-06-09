import argparse
import PcrParser


def Main():
	parser = argparse.ArgumentParser()
	parser.add_argument("file_path", 
	help = "the path to your raw rna ct data csv file for relative expression analysis",
	type = str)
	
	parser = argparse.ArgumentParser()
	
	parser.add_argument("file_name", 
	help = "The name of your raw rna ct data csv file for relative expression analysis",
	type = str)
	
	parser.add_argument("pos_group", 
	help = "The name of your positive experimental group",
	type = str)
	
	parser.add_argument("neg_group", 
	help = "The name of your negative experimental group",
	type = str)
	
	parser = argparse.ArgumentParser()
	parser.add_argument("output_file_name", 
	help = "The name of your raw rna ct data csv file for relative expression analysis",
	type = str)
	
	args = parser.parse_args()
	
	rna_parser = PcrParser(args.file_path,args.pos_group, args.neg_group)
						   
	input_table = rna_parser.input_table(args.file_name)
	
	input_table = rna_parser.format_table()
	
	rna_parser.save_table_to_csv(args.output_file_name)
	
	
if __name__=='__main__':
	Main()
						   
 	
							 
							 
	