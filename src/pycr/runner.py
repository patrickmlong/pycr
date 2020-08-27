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
	help = "The name of your normalizing reference transcript",
	type = str)
    parser.add_argument("target",
	help = "The name of your target transcript",
	type = str)

    args = parser.parse_args()
    rna_parser = PcrParser(args.file_path,
                           args.control,
                           args.normalizer,
                           args.target)

    input_table = rna_parser.load_table()
    rna_parser.check_columns(input_table)
    formatted_table = rna_parser.format_table(input_table)
    output_path = rna_parser.make_output_path()
    rna_parser.save_table_to_csv(formatted_table, output_path)
    rna_parser.visualize_rt(formatted_table, output_path)

if __name__=='__main__':
	main()
