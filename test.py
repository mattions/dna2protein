#!/usr/bin/env python

import subprocess
import filecmp
import glob
import yaml

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

def test_cwl_result(filename):
    cmdline = "rabix {0} -- --dna dna.txt".format(filename)
    subprocess.call(cmdline.split(" "))
    output_dir = filename.replace(".cwl", "")
    output_rna = glob.glob("{0}-*/root/transcribe/rna.txt".format(output_dir))[0]
    output_protein = glob.glob("{0}-*/root/translate/protein.txt".format(output_dir))[0]
    _compare_files(output_rna, STORED_RNA)
    _compare_files(output_protein, STORED_PROTEIN)

def create_temp_cwl(image_tag, original_cwl):
    
    temp_cwl = "{0}.tmp.cwl".format(image_tag.replace(":", "_"))
    f = yaml.safe_load(open(original_cwl))
    
    for step in [0, 1]:
        f['steps'][step]['run']['requirements'][0]['dockerPull'] = image_tag 

    with open(temp_cwl, "w") as yaml_test:
        yaml.dump(f, yaml_test)
    return temp_cwl

def build_docker():
    sha = subprocess.check_output("git log -1 --pretty=format:%H".split(" "))
    image_tag = "dna2protein:{0}".format(sha.decode("ascii"))
    cmdline =  "docker build -t {0} .".format(image_tag)
    # build docker image
    subprocess.call(cmdline.split(" "))
    return image_tag
    
    
    

if __name__ == "__main__":
    image_tag = build_docker()
    temp_cwl = create_temp_cwl(image_tag, "dna2protein.cwl")
    test_cwl_result(temp_cwl)
    