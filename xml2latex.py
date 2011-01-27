#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from xml.dom import minidom

indentLevel = 0

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
	if isOpening:
		print getIndents() + "\\begin{" + N.tagName + "}"
		indentLevel += 1
	else :
		indentLevel -= 1	
		print getIndents() + "\\end{" + N.tagName + "}"
	
def handleCommand(N, isOpening):
	if(isOpening): print getIndents() + "\\" + N.tagName

def handleParametrizedCommand(N, isOpening):
	if(isOpening):
		output = getIndents() + "\\" + N.tagName
		for k in N.attributes.keys(): output += "{" + N.attributes[k].value + "}"
		output += "{" + N.childNodes[0].data + "}"

		print output

def handleNode(N, isOpening):
	if N.nodeType == N.ELEMENT_NODE and len(N.childNodes) == 1 and N.childNodes[0].nodeType == N.TEXT_NODE: handleParametrizedCommand(N, isOpening)
	elif N.nodeType == N.ELEMENT_NODE and len(N.attributes) == 0 and len(N.childNodes) == 0: handleCommand(N, isOpening)
	elif N.nodeType == N.ELEMENT_NODE: handleEnvironment(N, isOpening)
	
xmlFile = minidom.parse(sys.argv[1])
explore(xmlFile)
