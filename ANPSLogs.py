#---------------------------------------------------------------------
# Grant De La Campa
# @2019
# ANPSLogs.py
# Functions:
#---------------------------------------------------------------------

import os
import datetime
from ANPSFormat import *


view = ['1', 'V', 'v', 'View', 'view']
store = ['2', 'S', 's', 'Store', 'store']
purge = ['3', 'P', 'p', 'Purge', 'purge']
retreive = ['4', 'R', 'r', 'Retreive', 'retreive']
quits = ['5', 'quit', 'exit', 'Exit', 'Quit', 'E', 'e', 'q', 'Q']

yes = []
no = []
logList = []

def logMenu():
    breakpoint("Menu")
    print("1: View")
    print("2: Store")
    print("3: Purge")
    print("4: Retreive")
    print("5: Exit")
    
def propogateLogList():                                            
    for item in os.listdir(os.getcwd()):
        if item.endswith('.log'):
            if item in logList:                                  # The log file has been recognized by ANPS
                print("-", item)
            else:                                                # Add the log file to ANPS List of Logs
                print("add", item)
                logList.append(item)
def viewLogs():
    breakpoint("VIEW")
    for item in logList:
        print("     -", item)

def storeLog(p_log):
    breakpoint("STORE")
    now = datetime.datetime.now()                               # get current info to build the log name 
    name = ("Log_" +
           str(now.month) +
           "_" + str(now.day) +
           "_" + str(now.year) +
           ".log")
    if os.path.exists(name):                                    # log exists so overwrite the log 
        print("this log already exists...")                     # TODO allow for overwite of this log. 
    else:
        with open(name, "w") as file:
            for item in p_log:
                print("Writing: ", item)
def purgeLog():
    breakpoint("PURGE")
    print("Select a Log to purge by number or * to purge all...")
    viewLogs()
    propogateLogList()                                          # rebuild the log list 
    
def logMain(p_log):
    propogateLogList()                                          # Find all current logs in the program 
    while(True):
        logMenu();
        answer = input(">> ")
        if answer in view:
            viewLogs()
        elif answer in store:
            storeLog(p_log)
        elif answer in purge:
            print("purge")
        elif answer in retreive:
            print("retreive")
        elif answer in quits:
            break;
        else:
            eHandler(answer)

logMain(["1", "2", "3", "4"])
