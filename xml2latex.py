#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ====================================================================
# Author : Maxime Gaudin
# Name : xml2latex
# ====================================================================
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import os
import getopt
from xml.dom import minidom

indentLevel = 0
environments = set([])
commands = set([])

preambule = "% Exported Preambule\n"
code = "% Exported code\n"

def getIndents():
	global indentLevel
	return '\t' * indentLevel

def explore(xmlInput):
	for N in xmlInput.childNodes:
		handleNode(N, True)
		explore(N)
		handleNode(N, False)

def handleEnvironment(N, isOpening):
	global indentLevel
	global environments
	global code
	
	if isOpening:
		code += getIndents() + "\\begin{" + N.tagName + "}\n"
		indentLevel += 1
		code += getIndents() + "\\" + N.tagName + "Header\n"
		environments.add(N.tagName)
	else :
		indentLevel -= 1	
		code += getIndents() + "\\end{" + N.tagName + "}\n"
	
def handleCommand(N, isOpening):
	global commands
	global code

	if(isOpening):
		output = getIndents() + "\\" + N.tagName
		commands.add(N.tagName)

		for k in N.attributes.keys(): output += "{" + N.attributes[k].value + "}" 	# Handle attributes
		if len(N.childNodes) == 1: output += "{" + N.childNodes[0].data + "}"		# Handle datas

		code += output + "\n"

def handleNode(N, isOpening):
	if N.nodeType == N.ELEMENT_NODE:
		if len(N.childNodes) == 0 or len(N.childNodes) == 1 and N.childNodes[0].nodeType == N.TEXT_NODE: handleCommand(N, isOpening)
		else: handleEnvironment(N, isOpening)

def generatePreambule():
	global preambule
	for e in environments: 
		preambule += "\\newenvironment{" + e + "}\n{\n}\n{\n}\n\n"
		preambule += "\\newcommand{\\" + e + "Header}{}\n\n"
	for c in commands : preambule += "\\newcommand{\\" + c + "}[]\n{\n}\n\n"

def usage():
	print "usage: python xml2latex.py [args] [option]"
	print ""
	print "List of arguments :"
	print "    --input (-i) : Specifies the input file."
	print ""
	print "List of options :"
	print "    --output (-o) : Specifies the output file. (Default : stdout)"
	print "    --print-preambule (-p) : Generate preambule. (Default : True)"
	print "    --print-code (-p) : Generate code. (Default : True)"
	print "    --help (-h) : Print this text."
	print ""
	print "Author : Maxime Gaudin (2011)"

def writeStringIntoFile(Str, Filename):
	try:
		f = open(Filename, "w")
		f.write(Str)
		f.close()
	except:
		sys.stderr.write("Error while writing ouput file")

try:
	opts, args = getopt.getopt(sys.argv[1:], "hi:o:pc", ["help", "input=", "output=", "print-preambule", "print-code"])
except getopt.GetoptError, err:
	print str(err) # will print something like "option -a not recognized"
	usage()
	sys.exit(2)

inputFilename=""
outputFilename=""
enablePreambule=False
enableCode=False

for o, a in opts:
	if o in ("-h", "--help"): usage()

	elif o == "-p": enablePreambule=True
	elif o == "-c": enableCode=True

	elif o in ("-i", "--input"): inputFilename=a
	elif o in ("-o", "--output"): outputFilename=a

	else: assert False, "Unhandled option"	

if inputFilename=="": 
	sys.stderr.write("You must specifie an input file (-i) !\n")
	usage()
	exit(1)

if enablePreambule == enableCode == False: 
	enablePreambule = True
	enableCode= True

try: 
	xmlFile = minidom.parse(inputFilename)
except: 
	sys.stderr.write("** Bad formed xml file. Parse aborted.\n")
	exit(1)

try:
	explore(xmlFile)
	if enablePreambule: generatePreambule()
except: 
	sys.stderr.write("** Oups ! Error during exploration.\n")
	exit(1)

output=""
if enablePreambule: output +=  preambule.encode('utf-8', 'ignore')
if enableCode: output += code.encode('utf-8', 'ignore')

if outputFilename == "": print output
else: writeStringIntoFile(output, outputFilename)
