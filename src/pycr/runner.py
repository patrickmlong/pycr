import argparse
import logging
from pycr.pcrparser import PcrParser


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", 
	help = "The path to a rna cycle threshold data (csv) for delta ct relative RNA quantification",
	type = str)
	
    parser.add_argument("experimental",
	help = "The name of your experimental group",
	type = str)
	
    parser.add_argument("control",
	help = "The name of your control group",
	type = str)

    args = parser.parse_args()
    rna_parser = PcrParser(args.file_path,args.experimental, args.control)
    
    input_table = rna_parser.input_table()
    input_table = rna_parser.format_table()
    rna_parser.save_table_to_csv()
    rna_parser.visualize_rt() 

if __name__=='__main__':
	main()
