#!/usr/bin/env python
from lxml import etree as ET

file_name = "UserMotions.xml"
doc = ET.parse(file_name)
root = doc.getroot()
#=====================================
def getMovements():
  global root
  listMove=list()
  for instruction in root:
    listMove.append(instruction.attrib['name'])
  return listMove
#=====================================
def appendMovement(aName, aType):
  global root
  global doc
  global file_name
  b = ET.Element('Instruction', name = aName,typemove = aType)
  root.append(b)
  doc.write(file_name)
# =====================================
def removeMovement(aMove):
  global root
  global file_name
  for instruction in root:
    if instruction.attrib['name'] == aMove:
      parent=instruction.getparent()
      parent.remove(instruction)
      doc.write(file_name)
#=====================================
def findDuplicates(aMove):
  aList = getMovements()
  result = False
  for aStr in aList:
    if aStr.lower() == aMove.lower():
      result = True
      break
  return result