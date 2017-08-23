import re
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("intersect")
    args = parser.parse_args()
    genere = re.compile(r'gene_id "(.*?)"')
    symbolre = re.compile(r'gene_name "(.*?)"')
    with open(args.intersect) as in_handle:
        for line in in_handle:
            genes = re.findall(genere, line)
            symbols = re.findall(symbolre, line)
            if len(set(genes)) == 1:
                continue
            else:
                print ":".join(genes), ":".join(symbols)
