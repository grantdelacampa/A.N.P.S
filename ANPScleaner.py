#---------------------------------------------------------------------
# Grant De La Campa
# @2019
# ANPScleaner.py
#---------------------------------------------------------------------

import os
import fnmatch

#---------------------------------------------------------------------------------
#           Format
#---------------------------------------------------------------------------------

from ANPSFormat import *

#---------------------------------------------------------------------------------
#           GLOBALS 
#---------------------------------------------------------------------------------

#the list of items polled from the subdirectories 
MasterList = []

#the list of items polld fromt he download directory 
downloads = []

#the list of sub directories
dirList = []

#list of paths to files that need deleting
delList = []

#---------------------------------------------------------------------------------
#           MENU KEYS
#---------------------------------------------------------------------------------

yList = ["Y", "y", "yes", "Yes", "YES"]
nList = ["N", "n", "no",  "No", "NO"]

#---------------------------------------------------------------------------------
#           FILE COLLECTORS
#---------------------------------------------------------------------------------

def build_master(mainDir, subDir):
    for item in subDir:
        tempPath = mainDir + item                                           # build the full path for each subdirectory 
        if(os.path.exists(tempPath) != False):                              # Verify the validity of the full path
            for sub in os.listdir(tempPath):                                # Retreive each file in the sub directory
                if (os.path.isfile(sub) == False):                          # checks if the sub directory is a file
                    filePath = tempPath + "/" + sub                         # Builds the path to the non-folder file
                    sub_noExt = os.path.splitext(sub)[0] + "*"              # places a wildcard at the end of the file name
                    MasterList.append(sub_noExt)                            # send to the master list
                    
def build_downloads(dlDir):
    if(os.path.exists(dlDir) != False):                                     # verify the download path
            for sub in os.listdir(dlDir):                                   # retreive files in the download directory
                if (os.path.isfile(sub) == False):                          # ignore the folders
                    downloads.append([sub, dlDir + "/" + sub])              # send to the downloads list [<file_name>, <file_path>]

#---------------------------------------------------------------------------------
#           FILE MATCHING
#---------------------------------------------------------------------------------
def comb_downloads():
    breakpoint("Comparing")
    print("Checking:", len(MasterList) + len(downloads), "items")
    print("Running: ", len(MasterList) * len(downloads), " comparisons")
    for i in range(0, len(MasterList)):                                     # get the indicies of the master list
        temp = "" + MasterList[i]                                           # build a temp string from the file name
        for item in downloads:                                              # get the file names from downloads
            if fnmatch.fnmatch(item[0], temp):                              # check if the master wild card matches with a downloads file [0, X]
                delList.append(item[1])                                     # build a delete list from the matching files coresponding path [x, 1]

#---------------------------------------------------------------------------------
#           FILE REMOVAL
#---------------------------------------------------------------------------------

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
                    try:
                        os.remove(delList[i])                                   # actually perform the delete here
                        print("removing:", delList[i])
                    except OSError as e:                                        # file might not exist
                        eHandler("Path>", delList[i])
                        print ("Failed with:", e.strerror)
                        print ("Error code:", e.code)
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

#---------------------------------------------------------------------------------
#           INTERFACE
#---------------------------------------------------------------------------------
def cleaner_start(mDir, dDir, sDir):        
    build_master(mDir,sDir)
    build_downloads(dDir)
    comb_downloads()
    del_downloads()
    purge_lists()
