import argparse
import glob 
import pickle
from rdflib import Graph 
import re

'''
python3 make_pickles.py --files ../ttl/schema/*.ttl &
python3 make_pickles.py --files ../ttl/t*/*.ttl &
python3 make_pickles.py --files ../ttl/relations/*.ttl &
python3 make_pickles.py --files ../ttl/places/*.ttl &
python3 make_pickles.py --files ../ttl/labels/*.ttl &
python3 make_pickles.py --files ../ttl/events/*.ttl &
python3 make_pickles.py --files ../ttl/actors/*.ttl &
'''

def main():

    parser = argparse.ArgumentParser()
    
    parser.add_argument('-l', '--limit', type=int, default=None, help='Limit the number of results, for faster testing')
    
    parser.add_argument('-i', '--files', type=str, default="ttl", nargs='+', help='input folder')
    
    opts = parser.parse_args()
    
    for f in opts.files:
        try:
            g = Graph()
            print("Parsing file {}".format(f))
            g.parse(f, format="turtle")
            
            print("Parsed {} triples from {}".format(len(g), f))

            if len(g):
                outfile = re.sub(r'\.ttl$', '.pickle', f)
                pickle.dump(g, open( outfile, "wb" ) )
                print("Exported pickle file {}".format(outfile))
        
        except Exception as e:

            print("Failed to parse {}".format(f))
            print("error: {}".format(e))

"""
reading:
g=Graph()
g += pickle.load(open( f, "rb" ))
"""

if __name__ == "__main__":
    main()