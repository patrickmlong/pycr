import argparse
from pycr.pcrparser import PcrParser
import sys

def parse_args(args):
    """Parse command line parameters
    Args:
      args ([str]): command line parameters as list of strings
    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """    
    parser = argparse.add_argument(
        "file_path",
        help="The path to raw ct data (csv) for relative RNA quantification",
        type=str,
    )
    parser.add_argument("control", help="The name of your control group", type=str)
    parser.add_argument(
        "normalizer", help="The name of your normalizing reference transcript", type=str
    )
    parser.add_argument("target", help="The name of your target transcript", type=str)
    
    return parser.parse_args(args)      
        
def main(args):
    args = parse_args(args)

    rna_parser = PcrParser(args.file_path, args.control, args.normalizer, args.target)

    raw_table = rna_parser.load_table()
    rna_parser.check_columns(raw_table)
    ddct_table = rna_parser.calculate_ddct(raw_table)
    output_path = rna_parser.make_output_path()
    rna_parser.save_table_to_csv(ddct_table, output_path)
    rna_parser.visualize_rt(ddct_table, output_path)

    
def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])

    
if __name__ == "__main__":
    run()
