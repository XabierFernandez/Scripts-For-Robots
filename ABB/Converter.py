#!/usr/bin/env python
"""
This program is intended to give an easy tool to convert
instructions in ABB .mod files from asterisk (*) to Robtarget points.
Python implementation by: Xabier Fernandez
Email :xabier.fernandez@outlook.com
version : 0.1
"""

import tkinter as tk
import sys,os.path
from tkinter import filedialog
import tkinter.messagebox as mbox

#==================== Declarations ============================================
######################################
master = tk.Tk()
E1 = None
E2 = None
E3 = None
######################################

FILEOPENOPTIONS = dict(defaultextension='.mod',
                  filetypes=[('All files','*.*'), ('MOD file','*.mod')])

keyWordsFile = ['MoveL','MoveJ','ArcL','ArcStart','ArcEnd','SpotL','SpotJ']
file_object=None
file_object1=None
fileArray = list()
subFileArray = list()
file_path = None
file_name = None
prefix = ''
suffix = ''
excludedInstructions = []

#===============================================================================

########## Target File ############
def getTargetFile():
    global file_object
    global file_name

    root = tk.Tk()
    root.withdraw()
    try:
        file_path = filedialog.askopenfilename( initialdir="/", title="Select file",
                                                     filetypes=(("MOD files", "*.mod"), ("all files", "*.*")))

        file_object = open(file_path, 'r')
        file_name = ( os.path.splitext (file_path)[0])

    except FileNotFoundError:
        Mbox('WARNING!', 'Target file not found.')
        sys.exit(0)

def readTargetFileLines():
    global file_object
    global fileArray

    for line in file_object.readlines ():
        fileArray.append(line)
    file_object.close()

def checkLines():
    global fileArray
    global prefix
    global suffix

    pointnum = 1
    s = ''
    for line in range(len(fileArray)):
        if checkRules(fileArray[line]):
            s1 = fileArray[line]
            s2 = fileArray[line]
            start = s2.find('[[')
            end = s2.find (']]')
            s2=s2[start:end+2]
            subFileArray.append(s2)
            fileArray[line] = s1.replace ( s2, prefix + str( pointnum ) + suffix )
            pointnum = pointnum + 1
            
def checkStrInLists(aStr, aList):
    return (any(x in aStr for x in aList))
     

def checkCharInStr(aChar, aStr):
    return (aChar in aStr)

def checkRules(aStr):
    global excludedInstructions
    global keyWordsFile

    return checkStrInLists ( aStr, keyWordsFile ) and not checkStrInLists ( aStr,excludedInstructions ) \
            and not checkCharInStr ( '!', aStr ) and checkCharInStr ( '[[', aStr )
    

########## Modified File ##########

def createModFile():
    global file_object1
    global file_name

    try:
        file_object1 = open ( os.path.join(file_name + '_copy.mod'),'w+')
    except FileNotFoundError:
        Mbox('WARNING!', 'Target file not found.')
        sys.exit(0)

def writeToModFile():
    global file_object1

    for line in range ( len ( fileArray ) ):
        if ('MODULE' in fileArray[line].upper () and 'ENDMODULE' not in fileArray[line].upper () ):
            file_object1.write ( fileArray[line] )
            for line1 in range ( len ( subFileArray ) ):
                file_object1.write('LOCAL CONST robtarget ' + prefix + str(line1+1) + suffix + ':=' + subFileArray[line1] + '\n' )
        else:
            file_object1.write ( fileArray[line] )
    file_object1.close ()

########### GUI features ###################

def Mbox(title, text):
    window = tk.Tk()
    window.wm_withdraw()
    mbox.showinfo(title, text)

def makeEntry():
    global E1
    global E2
    global E3

    tk.Label ( master, text="Prefix" ).grid ( row=0 )
    tk.Label ( master, text="Suffix" ).grid ( row=1 )
    tk.Label ( master, text="Excluded Instructions" ).grid ( row=2 )

    E1 = tk.Entry ( master )
    E2 = tk.Entry ( master )
    E3 = tk.Entry ( master )

    E1.grid ( row=0, column=1 )
    E2.grid ( row=1, column=1 )
    E3.grid ( row=2, column=1 )

    tk.Button ( master, text='Quit', command=quitEntry ).grid ( row=4, column=0, sticky=tk.W, pady=4 )
    tk.Button ( master, text='Continue', command=getEntryFields ).grid ( row=4, column=1, sticky=tk.W, pady=4 )

    tk.mainloop ()

def getEntryFields():
    global master
    global E1
    global E2
    global E3
    global prefix
    global suffix
    global excludedInstructions

    prefix = E1.get ()
    suffix = E2.get ()
    if not E3.get():
        excludedInstructions = '#,#'.split ( ',' )
    else:
        excludedInstructions = E3.get().split(',')

    master.quit ()

def quitEntry():
    global master

    master.quit ()
    sys.exit ( 0 )

#############################################

def main():
    makeEntry()
    getTargetFile()
    readTargetFileLines()
    checkLines ()
    createModFile ()
    writeToModFile ()

main()
