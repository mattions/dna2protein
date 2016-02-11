#!/usr/bin/env python
import argparse
from transcribe import VERSION

FILENAME_OUTPUT = "peptide.txt"

def translate(args):
    
    print "Welcome to translate, version: {0}".format(VERSION)
    mRNA = args['mRNA'].read().strip()
    codon_map = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

    protein = ''
    # find the start codon and proceed until a 'STOP'
    start = mRNA.find('AUG')
    if start != -1:
        while start+2 < len(mRNA):
            protein += codon_map[mRNA[start:start+3]]
            start += 3
        protein = protein[:protein.find('STOP')]
        with open(FILENAME_OUTPUT, "w") as output:
            output.write(protein)
            if args['verbose']:
                print "Protein has been transcribed. Result in {0}".format(FILENAME_OUTPUT)
        
    else:
        msg = "No AUG found as starting codon in your mRNA input. This program translates only mRNA "
        msg += "from eukaryotes: https://en.wikipedia.org/wiki/Start_codon"
        print msg
    print "Done."

if __name__ == "__main__":
    """ Parse the command line arguments """
    parser = argparse.ArgumentParser(description="Transcribe the provided mRNA into a peptide.", 
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("mRNA", type=argparse.FileType('r'), help="mRNA to transcribe")
    parser.add_argument("--verbose", "-v", help="Run in verbose mode", action="store_true")
    parser.add_argument("--version", action='version', version=VERSION)
    args = vars(parser.parse_args())

    """ Run the main method """
    translate(args)