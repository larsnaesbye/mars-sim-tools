# coding=utf-8
# Mars Simulation Project
# Script for making the HTML5 user guide files for resources and processes
# replaces the previous java-based internal code
# htmlgenerate.py
# @version 3.08 2015-05-26
# @author Lars Næsbye Christensen
#
# Usage : 'python htmlgenerate.py [xmldir] [htmldir]' 
# must match the current '-help' functionality currently in the Java code

import io
import os
import sys

# TODO: we should check for empty args first
xmldir = sys.argv[1]; # path to XML files from command line 
htmldir = sys.argv[2]; # path to generated HTML files from command line

# Open our sample file
f = open('resources.xml')
g = open('resources.html','w')

lines = f.readlines() # and read the lines

docheader ="<!DOCTYPE html>\n<head><title>Generic title</title>\n</head>"

for line in lines:
	if line == "\n":
		print "Skipped empty line..."  # ignore empty lines
	else:
		print line
f.close()
g.close()
