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
from xml.dom import minidom

indentLevel = 0
environments = Set([])
commands = Set([])

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

	if isOpening:
		print getIndents() + "\\begin{" + N.tagName + "}"
		indentLevel += 1
		environments.add(N.tagName)
	else :
		indentLevel -= 1	
		print getIndents() + "\\end{" + N.tagName + "}"
	
def handleCommand(N, isOpening):
	global commands

	if(isOpening):
		output = getIndents() + "\\" + N.tagName
		commands.add(N.tagName)

		for k in N.attributes.keys(): output += "{" + N.attributes[k].value + "}" 	# Handle attributes
		if len(N.childNodes) == 1: output += "{" + N.childNodes[0].data + "}"		# Handle datas

		print output

def handleNode(N, isOpening):
	if N.nodeType == N.ELEMENT_NODE:
		if len(N.childNodes) == 0 or len(N.childNodes) == 1 and N.childNodes[0].nodeType == N.TEXT_NODE: handleCommand(N, isOpening)
		else: handleEnvironment(N, isOpening)

def printUsage():
	print "**** XML to LaTeX converter              ****"
	print "**** Usage : python xml2latex [YourFile] ****"

if len(sys.argv) == 1: printUsage()
else:
	try: 
		xmlFile = minidom.parse(sys.argv[1])
		explore(xmlFile)
	except: sys.stderr.write("** Bad formed xml file. Parse aborted.")
