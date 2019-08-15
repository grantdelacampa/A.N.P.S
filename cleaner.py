import os
import fnmatch
from ANPSFormat import *


MasterList = []
downloads = []

dirList = []
delList = []

yList = ["Y", "y", "yes", "Yes", "YES"]
nList = ["N", "n", "no",  "No", "NO"]

mDate = ""

##TODO:
##    - Make this into a class
##    - remove bootSequence and the getter methods!!!
##    - this can be pulled from DNMboot.py


#------------------------------------------------------------REMOVE FROM HERE---------------------------------------------------------------------
def bootSequence():
    with open("DNM.anp", "r") as text:
        inList = text.readlines()
        if(inList):                                                                             #VALIDATE: DNM.anp is not empty.
            if(os.path.exists(inList[0][0:-1])) & (os.path.exists(inList[1][0:-1])):            #VALIDATE: DNM.anp contains proper directories.
                for item in range(0,len(inList)):
                    dirList.append(inList[item][0:-1])      #[0:-1] removes the new line character
                mDate = os.path.getmtime("DNM.anp")
            else:
                raise BufferError("DNM.anp contains malformed directories")
        else:
            raise BufferError("DNM.anp does not contain any directories")
def getDownloads():
    if(dirList):
        return dirList[1]
def getMain():
    return dirList[0]
def getSub():
    if(dirList):
        subList = []
        for item_num in range(2, len(dirList)):
            subList.append(dirList[item_num])
        return subList
    else:
        return "ERROR dirList is empty"

#-----------------------------------------------------------------TO HERE---------------------------------------------------------------------------

def build_master():
    for item in getSub():
        tempPath = getMain() + item                                         # build the full path for each subdirectory 
        if(os.path.exists(tempPath) != False):                              # Verify the validity of the full path
            for sub in os.listdir(tempPath):                                # Retreive each file in the sub directory
                if (os.path.isfile(sub) == False):                          # checks if the sub directory is a file
                    filePath = tempPath + "/" + sub                         # Builds the path to the non-folder file
                    sub_noExt = os.path.splitext(sub)[0] + "*"              # places a wildcard at the end of the file name
                    MasterList.append(sub_noExt)                            # send to the master list
                    
def build_downloads():
    dl = getDownloads()
    if(os.path.exists(dl) != False):                                        # verify the download path
            for sub in os.listdir(dl):                                      # retreive files in the download directory
                if (os.path.isfile(sub) == False):                          # ignore the folders
                    downloads.append([sub, dl + "/" + sub])                 # send to the downloads list [<file_name>, <file_path>]
                    
def comb_downloads():
    breakpoint("Comparing")
    print("Checking:", len(MasterList) + len(downloads), "items")
    print("Running: ", len(MasterList) * len(downloads), " comparisons")
    for i in range(0, len(MasterList)):                                     # get the indicies of the master list
        temp = "" + MasterList[i]                                           # build a temp string from the file name
        for item in downloads:                                              # get the file names from downloads
            if fnmatch.fnmatch(item[0], temp):                              # check if the master wild card matches with a downloads file [0, X]
                delList.append(item[1])                                     # build a delete list from the matching files coresponding path [x, 1]
                
def del_downloads():
    if(delList):
        print("Number of matches found:", len(delList))
        for i in range(0, len(delList)):
            print("  -", delList[i])
        print("Would you like to delete the listed files?")
        while(1):
            answer = input("Y/N> ")
            if answer in yList:
                for i in range(0, len(delList)):                                # size the range dynamically based on the size of the deletion list. 
                    os.remove(delList[i])                                       # actually perform the delete here
                    print("removing:", delList[i])
                break
            elif answer in nList:
                print("Exiting cleaner_start()")
                break;
            else:
                print("Error ", answer, "is invalid")
    else:
        print("No duplicate files found....")
        
        
        

def purge_lists():                                      # Zeros lists for next run if needed
    del MasterList[:]
    del downloads[:]
    del dirList[:]
    del delList[:]
    
def cleaner_start():        
    bootSequence()          # Change to DNMboot.py
    build_master()
    build_downloads()
    comb_downloads()
    del_downloads()
    purge_lists()

#cleaner_start()
