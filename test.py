#!/usr/bin/env python

import subprocess
import filecmp
import glob

STORED_RNA = "data/stored/rna.txt"
STORED_PROTEIN = "data/stored/protein.txt"

def _compare_files(computed_file, stored_file):
    try:
        assert(filecmp.cmp(computed_file, stored_file))
    except AssertionError as e:
        print ("\nThese files are different!!! {0} is not equal to {1}\n".format(computed_file, stored_file))
        raise e

def test_output():
    cmdline_transcribe = "./transcribe.py dna.txt"
    subprocess.call(cmdline_transcribe.split(" "))
    cmdline_translate = "./translate.py rna.txt"
    subprocess.call(cmdline_translate.split(" "))
    _compare_files("rna.txt", STORED_RNA)
    _compare_files("protein.txt", STORED_PROTEIN)

def test_cwl_result():
    cmdline = "rabix dna2protein.cwl.json -- --dna dna.txt"
    subprocess.call(cmdline.split(" "))
    
    output_rna = glob.glob("dna2protein.cwl-*/root/transcribe/rna.txt")[0]
    output_protein = glob.glob("dna2protein.cwl-*/root/translate/peptide.txt")[0]
    _compare_files(output_rna, STORED_RNA)
    _compare_files(output_protein, STORED_PROTEIN)
    
if __name__ == "__main__":
    test_output()
    test_cwl_result()
    