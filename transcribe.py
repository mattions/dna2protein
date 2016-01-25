#!/usr/bin/env python
import argparse
import re
import sys

def transcribe(args):
	# create a transcription map and use regex to translate
	map = {"A":"U", "T":"A", "C":"G", "G":"C"}
	map = dict((re.escape(k), v) for k, v in map.iteritems())
	pattern = re.compile("|".join(map.keys()))
	DNA = args['dna'].read().strip()
	mRNA = pattern.sub(lambda m: map[re.escape(m.group(0))], DNA)

	# write a verbose output to stderr and just mRNA to sdtout 
	if args['verbose']:
		print ("Your original DNA sequence: {0}".format(DNA))
		print ("Your translated mRNA sequence: {0}".format(mRNA))
	with open("rna.txt", "w") as output:
		output.write(mRNA)

if __name__ == "__main__":
	""" Parse the command line arguments """
	parser = argparse.ArgumentParser(description="Translates a DNA input test into a RNA")
	parser.add_argument("dna", type=argparse.FileType("r"))
	parser.add_argument("-v", "--verbose", action="store_true", default=False)
	# By setting args as var(...), it becomes a dict, so 'dna' is a key
	# Alternative use: args = parser.parse_args(), and 'dna' is an attr of args!
	# You must change how you call the args you parse based on this usage! 
	args = vars(parser.parse_args())

	""" Run the desired methods """
	transcribe(args)
