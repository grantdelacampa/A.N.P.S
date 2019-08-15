

#---------------------------------------------------------------------
# Grant De La Campa
# @2019
# ANPSLauncher.py
# Functions:
#---------------------------------------------------------------------

import os
import ANPS

import time
from ANPSsplash import *


exitCode = False
#ANPS.boot()
splashScreen()
os.system('cls')
while(exitCode != True):
    #Get the Exit code from ANPS when it terminates             NOTE: Should only occur after DNM Mod is run
    response = ANPS.main()
    if(response == 0):                                          # Break Response, exit code sent from ANPS so break main while and exit
        break;
    elif(response == 1):                                        # Refresh Response, restart code sent from ANPS due to file modification
        os.system('cls')
        print("Restarting ANPS.py....")
        time.sleep(5)                                           # allows Restart message to be read by user, adds flair |_O_|
        os.system('cls')                                        #                                                         |
        continue                                                #                                                        / \
    elif(response == 2):                                        # Continue response: Tells the main while to not exit and continure running ANPS.main()
        os.system('cls')
        continue
    else:                                                       # should never be reached
        print("ERROR ANPS.py terminated with an Unknown Exit Code: ", response)
        
