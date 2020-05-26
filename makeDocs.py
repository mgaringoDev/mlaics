# Imports
import os
from os import listdir
from os.path import isfile, join
import time, datetime
import re

import shutil
import glob
from pathlib import Path
import json

# Functions
def appendstr(strList):
    stOut = ''
    for st in strList:
        stOut = stOut + st + '\\' 

    return stOut

def getAllJupterFiles():
    cwd = os.getcwd()
    src= cwd+'\\__JupyterNotebooks\\'        

    fullPath = []
    fileName = []
    for path in Path(src).rglob('*.ipynb'):
        # not inside any of the checkpoints
        if str(path).find('ipynb_checkpoints')<0:
            fullPath.append(appendstr(str(path).split('\\')[:-1]) )       
            fileName.append(str(path).split('\\')[-1].split('.')[0])

            # used for debugging
            # print("*"*24)
            # print(fullPath[-1])            
            # print(fileName[-1])
            # print("*"*24)   
            # print("\n"*2)
    return fullPath, fileName

def removeExtra(fName):
    fNameNew = fName
    fNameNew = fNameNew.replace('-','_')        
    fNameNew = fNameNew.replace(' ','_')        
    return fNameNew

def copyFile(srcLocation,dstLocation,fileName):
    srcFile = srcLocation + fileName + '.ipynb'
    dstFile = dstLocation + removeExtra(fileName) + '.json'    
    shutil.copy(srcFile, dstFile)

def getListOfJupyterNotebooks():
    cwd = os.getcwd()
    src= cwd+'\\__JupyterNotebooks\\'
    onlyFiles = [f for f in listdir(src) if isfile(join(src, f))]
    fileName = []
    for file in onlyFiles:
        fileName.append(file.split('.')[0])
    
    return src, fileName

def getListOfJupyterNotebooks():
    cwd = os.getcwd()
    src= cwd+'\\__JupyterNotebooks\\'
    onlyFiles = [f for f in listdir(src) if isfile(join(src, f))]
    fileName = []
    for file in onlyFiles:
        fileName.append(file.split('.')[0])
    
    return src, fileName

def getDstLocation():
    cwd = os.getcwd()
    dst= cwd+'\\_data\\jupyterNotebooks\\'
    print(dst)
    return dst

def getNotesDstLocation():
    cwd = os.getcwd()
    dst= cwd+'\\pages\\jupyterNotebooks\\'
    return dst

def createJSONFiles():
    print('Now creating JSON files')
    fullPaths, fileNames = getAllJupterFiles()
    dstLocation = getDstLocation()   

    for fileName,fullPath in zip(fileNames,fullPaths):
    
        # Copy the file
        copyFile(fullPath,dstLocation,fileName)
        print(f"Converting {fileName}")               

    print('Finished creating JSON files')

def writeNote(fName,noteLocation,frontMatterCells):
    fName = removeExtra(fName)
    noteName = noteLocation + '\\'+ fName + '.md'
    print(f"Now creating {noteName}")
    
    with open(noteName, 'w') as fileOut:
        for line in frontMatterCells:
            if line.find('__AutoGenThis__')<0:                
                fileOut.write(line)
            else:                                
                if 'permalink' in line:
                    # found permalink
                    line = line.replace("__AutoGenThis__",(fName+".html"))                    
                    fileOut.write(line)

                if 'notebookfilename' in line:
                    # found permalink
                    line = line.replace("__AutoGenThis__",fName)
                    fileOut.write(line)

        fileOut.write('\n'*2)
        fileOut.write('{% include jupyterNotebook.html %}')
            
def createPages():
    print('Creating pages')
    fullPaths, fileNames = getAllJupterFiles()
    jsonLocation = getDstLocation() 
    notesLocation = getNotesDstLocation() 

    for fileName in fileNames:
        #if fileName == 'course_DataSchool_sklearn_10_categorical_features_pipeline':
        with open(jsonLocation+removeExtra(fileName)+'.json', 'r', encoding="utf8") as f:            
            data = json.load(f)

            for cell in data['cells']:
                # need to parse metadata and celltype here.
                #print(cell['metadata'])
                metaCell = cell['metadata']
                key = list(metaCell.keys())
                if len(key)>0:                    
                    key = key[0]
                    #print(metaCell[key])
                    metaValue = str(metaCell[key])

                if cell['cell_type'] == "markdown":                        
                    if metaValue == 'FrontMatter':                            
                        #print(cell['source'])
                        #print('Found Front Matter')
                        #print(notesLocation)
                        writeNote(fileName,notesLocation,cell['source'])
                        break

    print('Finished creating all pages')

def main():        
    createJSONFiles()
    createPages()

if __name__ == '__main__':
	main()