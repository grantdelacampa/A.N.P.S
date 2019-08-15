#---------------------------------------------------------------------
# Grant De La Campa
# @2019
# ANPSboot.py
# Functions:
#---------------------------------------------------------------------

import os.path
from ANPSFormat import *

# Create boot object 
class IO_BOOT():
    def __init__(self):
        self.dirList = []
        self.mDate = None
#----------------------------------------------------------------------------------
#           I/O FOR DIRECTORIES
#----------------------------------------------------------------------------------
# to be used only by IO_BOOT.bootLoad

    # Used for single directory with validation
    def bootLoop(self,message):
        mDir = ''
        while(True):
            print(message)
            mDir = input(">")
            if(os.path.exists(mDir)):
                break;
            else:
                print("ERROR: " + mDir + "is not a valid path")
        return mDir
    
    # Used for multi-directory input with out validation
    # validation is handled by ANPS.ErrorRecovery
    def classLoop(self):
        outStream = []
        while(True):
            print("Please enter the number of subfolders")
            numSubfolders = input("# of subfolders = ")
            if(numSubfolders.isdigit()):
                print("Entered: ", numSubfolders)
                print("Please Enter the name of each subfolder:")
                
                for i in range(0,int(numSubfolders)):
                    subFldr = input("../")
                    outStream.append(subFldr)
                break;
            else:
                eHandler(numSubFolders)
        return outStream
#----------------------------------------------------------------------------------
#           DIRLIST WRITER 
#----------------------------------------------------------------------------------

    def bootLoad(self):
        with open("DNM.anp", "r") as text:
            inList = text.readlines()
            if(inList):                                                                             #VALIDATE: DNM.anp is not empty.
                if(os.path.exists(inList[0][0:-1])) & (os.path.exists(inList[1][0:-1])):            #VALIDATE: DNM.anp contains proper directories.
                    for item in range(0,len(inList)):
                        self.dirList.append(inList[item][0:-1])      #[0:-1] removes the new line character
                    self.mDate = os.path.getmtime("DNM.anp")
                else:
                    raise BufferError("DNM.anp contains malformed directories")
            else:
                raise BufferError("DNM.anp does not contain any directories")
            
#----------------------------------------------------------------------------------
#           MAIN INTERFACE
#----------------------------------------------------------------------------------
# Intended to be the main interface for IO_BOOT
    def boot(self):                             #DNM.anp exists
        if os.path.isfile("DNM.anp"):
            self.bootLoad()                     # verify DNM.anp is healthy
            return 0;                           # return flag 0
        else:                                   # DNM.anp doesnt exists
            breakpoint("SETUP")
            print("NOTICE: The DNM.anp file appears to be missing.")
            print("ANPS will attempt to rebuild the DNM.anp file")
            mDir = ''
            entrys = []
            classDir = []
            entrys.append(self.bootLoop("Please Enter your Document Directory: "))      # retreive main directory (verification)
            entrys.append(self.bootLoop("Please Enter your Downloads Directory: "))     # retreive downlaod directoru (verification)
            classDir = self.classLoop()                                                 # retreive the sub directories from the user (no verification)
                                                                                        #   ^Errors handled by ANPS error recovery tool 
            with open("DNM.anp", "w") as file:                                          # create and write to DNM.anp
                for item in entrys:
                    file.write(item + "\n")
                for classFldr in classDir:
                    file.write("/" + classFldr + "\n")
            os.system('cls')
            self.bootLoad()

#----------------------------------------------------------------------------------
#           GETS
#----------------------------------------------------------------------------------
# GET calls to retreive data from DMN.anp
    def getMain(self):                                  # returns the main directory <C:/Users/<name>/<doucments>
        return self.dirList[0]  
    def getDownloads(self):                             # returns the download directory <C:/Users/<name>/<downloads> 
        return self.dirList[1]
    def getmDate(self):                                 # get the modified date 
        return self.mDate;
    def getSub(self):                                   # returns document sub-driectories for printing
        subList = []
        for item_num in range(2, len(self.dirList)):
            subList.append(self.dirList[item_num])
        return subList
