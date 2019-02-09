#---------------------------------------------------------------------
# Grant De La Campa
# @2019
# ANPS.py
# Functions:
#---------------------------------------------------------------------

import os
import os.path
import sys
import time
import datetime
import webbrowser
import win32print
import win32api
import dayCalculator
from datetime import date


#---------------------------------------------------------------------------------
#           GLOBALS & DIRECTORIES 
#---------------------------------------------------------------------------------

version = "V4"

mainDir = "C:/Users/grant/OneDrive/Documents"

dlDir = "C:/Users/grant/Downloads"

sublist = ["/CSC 134 Database Management Systems",
           "/CSC 159 Operating System Pragmatics",
           "/PHYS 11C",
           "/Music 127"]

if os.path.isfile("DNM.txt"):
    dnmDate = os.path.getmtime("DNM.txt")
else:
    with open("DNM.txt", "w") as file:
        file.write("DO NOT MODIFY")

printer = win32print.GetDefaultPrinter()

pLog = []
eLog = []
#---------------------------------------------------------------------------------
#           MENU KEYS
#---------------------------------------------------------------------------------

menuList = ['Menu','menu', 'M', 'm', 'options', 'o', 'O']
runList = ['1','Run','run','Run Script', 'R', 'r']
DNMList = ['2','DNM','DNM override', 'D', 'd', 'dnm']
scrubList = ['3','scub','Scrub','Scrub DL', 'S', 's']
logList = ['4','log','Log','l','L']
queueList =['5', 'print queue', 'queue', 'Q', 'q', 'Print queue', 'Print Queue']
infoList = ['6', 'I', 'i', 'Info', 'info', 'information']
helpList = ['7','help','Help', 'H', 'h']
exitList = ['8','Exit','Quit','quit','exit', 'E', 'e']
easterList = ['diablo']

#----------------------------------------------------------------------------------
#           FORMATING
#----------------------------------------------------------------------------------

def breakPoint(message):
    print("--------------------------------------------------------------------------------")
    print("          ", message)
    print("--------------------------------------------------------------------------------")

def eHandler(error):
    print("ERROR: ", error, " is not valid")

def listCalls(callList):
    calls = "     -Calls: "
    for item in callList:
        calls = calls + item + " "
    print(calls)
    print("--------------------------------------------------------------------------------")

#----------------------------------------------------------------------------------
#           PRINT SUBROUTINES
#----------------------------------------------------------------------------------

def printSubRoutine(docPath):
    print("        -Printing: ", docPath)
    try:
        win32api.ShellExecute(0,"print",docPath, '/d:"%s"' % win32print.GetDefaultPrinter(),".",0)
        time.sleep(5)
    except win32api.error:
        eLog.append(docPath)
        
    
def getDefault():
    print("Default Printer: ", win32print.GetDefaultPrinter())

def pErrors():
    if not eLog:
        print("PrintSubRoutine() completed with no errors")
    else:
        print("The Following documents encountered errors:  ")
        for item in eLog:
            print("        -",item)
    
#----------------------------------------------------------------------------------
#           DATE SUBROUTINES
#----------------------------------------------------------------------------------

def dateHandler(name, lower, upper):
    valid = False
    query = ''
    while(valid != True):
        query = input(name)
        if(query.isdigit()):
            entry = int(query)
            if entry in range(lower, upper):
                print(entry, "is in valid range")
                return entry
            else:
                eHandler(query)
        else:
            eHandler(query)
            
#----------------------------------------------------------------------------------
#           TIME SUBROUTINES
#----------------------------------------------------------------------------------

def setModTime():
    breakPoint("setting mod time...")
    now = datetime.datetime.now()
    then = datetime.datetime.fromtimestamp(os.path.getmtime("DNM.txt"))
    print("writing: ", datetime.datetime(now.year,now.month,now.day,now.hour,now.minute,now.second))
    print("overiding: ", datetime.datetime(then.year,then.month,then.day,then.hour,then.minute,then.second))
    modtime = time.mktime(now.timetuple())
    os.utime("DNM.txt",(modtime,modtime))

def overideModTime():
    breakPoint("Overide Mod Time")
    print("WARNING: overiding DMN.txt mod time may result in reprinting")
    print("Please verify you would like to continue..")
    modQ  = ''
    end = False
    while (end != True):        
        modQ = input("Y/N: ")
        if(modQ == 'Y') | (modQ == 'y'):
            print("Overriding DNM.txt")
            end = True
            year = dateHandler("Year:   ", 1970, datetime.datetime.now().year+1)
            month = dateHandler("Month:  ", 1, 13)
            day = dateHandler("Day:    ",1, dayCalculator.dayConstraint(year,month))
            hour = dateHandler("Hour:   ", 0, 24)
            minute = dateHandler("Minute: ", 0, 60)
            second = dateHandler("Second: ", 0, 60)
            modDate = datetime.datetime(year,month,day,hour,minute,second)
            modTuple = time.mktime(modDate.timetuple())
            os.utime("DNM.txt", (modTuple, modTuple))
            print("Modification complete DNM.txt set to: ", modDate)
            print("NOTICE: please exit ANPS for changes to take effect")
        elif(modQ == 'N') | (modQ == 'n'):
            print("Exiting subrouting overideModTime()")
            end = True
            #os.execl(sys.executable, sys.executable, * sys.argv)
        elif(modQ == 'C'):
            print("Current DNM: ", datetime.datetime.fromtimestamp(os.path.getmtime("DNM.txt")))
        else:
            eHandler(modQ)
            
    
#---------------------------------------------------------------------------------
#           DIRECTORY SUBROUTINES
#---------------------------------------------------------------------------------

def printer():
    breakPoint("PRINTING FROM DIRECTORIES")
    print("Begining directory search @" + mainDir)
    for extention in sublist:
        tempPath = mainDir + extention
        print("    In Directory: ", tempPath)
        for sub in os.listdir(tempPath):
            filePath = tempPath + "/" + sub
            if sub.endswith('.docx') | sub.endswith('.txt') | sub.endswith('.pdf'):
                if os.path.getmtime(filePath) >= dnmDate:
                    printSubRoutine(filePath)
                    pLog.append(sub)
    pErrors()
    setModTime()

def scrub():
    breakPoint("SCRUB DOWNLOADS")
    print("WARNING: This will delete files from:", dlDir)
    print("Please verify you would like to continue..")
    valid = False
    scrubQ = ''
    while(valid != True):
        scrubQ = input("Y/N: ")
        if(scrubQ == 'Y') | (scrubQ == 'y'):
            for item in os.listdir(dlDir):
                if item in pLog:
                    print("     -Removing: ", item)
                    os.remove(dlDir + "/" + item)
            valid = True
        elif(scrubQ == 'Y*'):
            print("Nuclear Option Selected...")
            for item in os.listdir(dlDir):
                print("     -Removing: ", item)
                os.remove(dlDir + "/" + item)
            valid = True
        elif(scrubQ == 'N') | (scrubQ == 'n'):
            print("Exiting subrouting scrub()")
            valid = True
        else:
            eHandler(scrubQ)
#I was listening to this song when I wrote this script, RIP.
def eggs():
    print("Who told you about this!?")
    webbrowser.open('https://www.youtube.com/watch?v=KlQESTshOPw')
    time.sleep(10)
    sys.exit()
    
#---------------------------------------------------------------------------------
#           MENU HELPERS
#---------------------------------------------------------------------------------

def info():
    breakPoint("INFO")
    print("A.N.P.S: Automated Network Printer Script")
    print("@Grant De La Campa")
    print("2019")
    print("Version: ", version)
    getDefault()
    
def helpM():
    breakPoint("HELP")
    print("#: Menu: ")
    print("     -Description: Launches the user menu to display options")
    listCalls(menuList)
    print("1: Run Script: ")
    print("     -Description: Fires off the print script to iterate on interal directories.")
    listCalls(runList)
    print("2: DNM override: ")
    print("     -Description: Allows the user to roll back the target date for printing.")
    print("                   Restricted to any year between 1/1/1970 and the current year.")
    listCalls(DNMList)
    print("3: Scrub DL: ")
    print("     -Description: If the log contains any files this will remove duplicates from ")
    print("                   the downloads folder.")
    listCalls(scrubList)
    print("4: Print Log: ")
    print("     -Description: Prints a log of the printed files after running the script")
    listCalls(logList)
    print("5: Queue")
    print("     -Description: Launches native browser to check queued files on printsmart")
    listCalls(queueList)
    print("6: Info: ")
    print("     -Description: Gives info about the program.")
    listCalls(infoList)
    print("7: Help: ")
    print("     -Description: The current menu being displayed, gives a list of commands.")
    listCalls(helpList)
    print("8: Quit: ")
    print("     -Description: Exit the ANPS shell")
    listCalls(exitList)

def menu():
    breakPoint("MENU")
    print("Select from the following...")
    print("1: Run Script")
    print("2: DNM override")
    print("3: Scrub DL")
    print("4: Print Log")
    print("5: Queue")
    print("6: Info")
    print("7: Help")
    print("8: Quit")

def log():
    breakPoint("LOG")
    if(pLog == []):
        print("Log is empty please run script to populate")
    else:
        for item in pLog:
            print("     -", item)

def queue():
    breakPoint("QUEUE")
    print("WARINING: This will launch your default Web Browser...")
    print("NOTE: Login information is required")
    print("Please verify you would like to continue..")
    valid = False
    webQ = ''
    while(valid != True):
        webQ = input("Y/N: ")
        if(webQ == 'Y') | (webQ == 'y'):
            webbrowser.open("https://printsmart.csus.edu/app?service=page/UserReleaseJobs")
            valid = True
        elif(webQ == 'N')| (webQ == 'n'):
            print("Exiting Subroutine Queue()")
            valid = True
        else:
            eHandler(webQ)
    
#---------------------------------------------------------------------------------
#           MAIN 
#---------------------------------------------------------------------------------
query = ''
print("A.N.P.S Shell" , version, "@2019")
menu()
while(query != 'Exit'):
    query = input("ANPS>> ")
    if(query == "") | (len(query)==0):
        eHandler(query)
    elif(query in runList):
        os.system('cls')
        printer()
    elif(query in DNMList):
        os.system('cls')
        overideModTime()
    elif(query in infoList):
        os.system('cls')
        info()
    elif(query in helpList):
        os.system('cls')
        helpM()
    elif(query in scrubList):
        os.system('cls')
        scrub()
    elif(query in logList):
        os.system('cls')
        log()
    elif(query in easterList):
        os.system('cls')
        eggs()
    elif(query in queueList):
        os.system('cls')
        queue()
    elif(query in menuList):
        os.system('cls')
        menu()
    elif(query in exitList):
        break
    else:
        eHandler(query)



    
