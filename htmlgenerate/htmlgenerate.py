# coding=utf-8
# Mars Simulation Project
# Script for making the HTML5 user guide files for resources and processes
# replaces the previous java-based internal code
# htmlgenerate.py
# @version 3.08 2015-05-14
# @author Lars Næsbye Christensen
#
# Usage : 'python htmlgenerate.py' 
# must match the current '-help' functionality currently in the Java code

import io
import os
import sys

xmldir = sys.argv[1]; // path to XML files from command line 
htmldir = sys.argv[2]; // path to generated HTML files from command line

