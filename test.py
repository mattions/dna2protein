#!/usr/bin/env python

import subprocess
import filecmp
import glob

def _compare_files(computed_file, stored_file):
    try:
        assert(filecmp.cmp(computed_file, stored_file))
    except AssertionError as e:
        print ("\nThese files are different!!! {0} is not equal to {1}\n".format(computed_file, stored_file))
        raise e

def test_result():
    cmdline = "rabix dna2protein.cwl.json -- --dna dna.txt"
    subprocess.call(cmdline.split(" "))
    stored_rna = "data/stored/rna.txt"
    stored_peptide = "data/stored/peptide.txt"
    output_rna = glob.glob("dna2protein.cwl-*/root/transcribe/rna.txt")[0]
    output_peptide = glob.glob("dna2protein.cwl-*/root/translate/peptide.txt")[0]
    _compare_files(output_rna, stored_rna)
    _compare_files(output_peptide, stored_peptide)
    
if __name__ == "__main__":
    test_result()