import argparse
import logging
from pycr.pcrparser import PcrParser


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", 
	help = "The path to ct data (csv) for relative RNA quantification",
	type = str)
	
    parser.add_argument("control",
	help = "The name of your control group",
	type = str)
    parser.add_argument("normalizer",
	help = "The name of your control group",
	type = str)
    parser.add_argument("target",
	help = "The name of your control group",
	type = str)



    args = parser.parse_args()
    rna_parser = PcrParser(args.file_path,
                           args.control,
                           args.normalizer,
                           args.target)
    
    input_table = rna_parser.input_table()
    input_table = rna_parser.format_table()
    rna_parser.save_table_to_csv()
    rna_parser.visualize_rt() 

if __name__=='__main__':
	main()
