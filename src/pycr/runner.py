import argparse
from pycr.pcrparser import PcrParser 


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("file_path", 
	help = "The path to your raw rna CT data csv file for delta CT RNA level analysis",
	type = str)
	
	parser.add_argument("experimental",
	help = "The name of your experimental group",
	type = str)
	
	parser.add_argument("control",
	help = "The name of your control group",
	type = str)
	
    # Run pycr using arguments
	args = parser.parse_args()
	
	rna_parser = PcrParser(args.file_path,args.experimental, args.control)
						   
	input_table = rna_parser.input_table()
	input_table = rna_parser.format_table()
	rna_parser.save_table_to_csv()
	
	
if __name__=='__main__':
	main()
