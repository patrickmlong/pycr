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

    #logging.basicConfig(level = logging.INFO)
    #logger = logging.getLogger("pycr")

    args = parser.parse_args()
    rna_parser = PcrParser(args.file_path,args.experimental, args.control)
    
    #logger.info(f"Loading input {args.file_path}")
    input_table = rna_parser.input_table()
    #logger.info("Formatting table")
    input_table = rna_parser.format_table()
    #logger.info("Saving table")
    rna_parser.save_table_to_csv()
    

if __name__=='__main__':
	main()
