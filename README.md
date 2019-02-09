# A.N.P.S
Automated Network Printing Script 
Description: 
  A pretty simple python script I wrote to manage course notes. Current iteration uses an auxilary file to timestamp the last print job. Using this time stamp the script knows to print documents added after the last run. Also contains a function to remove duplicate files located in the users downloads after the script has run.
Features:
  - Records printed documents and can remove them from your download folder. 
  - Automatic creation of the DNM.txt file if it does not exist.
  - Ability to check the printer queue when using CSUS printsmart services. 
  - Ability to override the last modification time of the DNM.txt file.
  - Easy to use shell based interface.
  - Sell clearing shell for ease of use. 
Requirments: 
  - Windows operating system
  - win32api required 
  - win32print required
  - Python 
  - User needs to change directory variables in the script. 
  - Printsmart must be set up for Campus use.
      -> See http://printsmart.csus.edu/help/mobility-print-devices/topics/en/client-setup.html
Notes: 
  - This script was intended to be used with the printsmart system used at California State University Sacramento. It is not guaranteed to     work with your home network printer. 
Known Bugs and Issues:
  - Some documents fail to print which are caught by a try/except block logged and displayed to the user after execution.
  - In IDLE os.system('cls') will flash a new window but will not clear the IDLE shell. This is not fixable and is the nature of IDLE.
  - Most likely there are spelling mistakes feel free to point them out. 
  - Linux and OS are not supported. 
  
  
