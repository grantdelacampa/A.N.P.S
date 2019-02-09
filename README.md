# A.N.P.S
Automated Network Printing Script 

Description: 
  A pretty simple python script I wrote to manage course notes. Current iteration uses an auxilary file named DNM.txt (Do Not Modify) to timestamp the last print job. Using this time stamp the script knows to print documents added after the last run and upon completion sets the documents mod time to the curent system time. Also contains several other functions to assist the user such as removing duplicate files located in the users downloads after the script has run.
  
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
      - See http://printsmart.csus.edu/help/mobility-print-devices/topics/en/client-setup.html
      
Notes: 
  - This script was intended to be used with the printsmart system used at California State University Sacramento. It is not guaranteed     to work with your home network printer. 
  - Printing uses the win32api to call shellexecute. 
      - See: https://docs.microsoft.com/en-us/windows/desktop/api/shellapi/nf-shellapi-shellexecutea
      
Known Bugs and Issues:
  - Some documents fail to print which are caught by a try/except block logged and displayed to the user after execution.
  - In IDLE os.system('cls') will flash a new window but will not clear the IDLE shell.
      - See: https://stackoverflow.com/questions/1432480/any-way-to-clear-pythons-idle-window
  - Most likely there are spelling mistakes feel free to point them out. 
  - Linux and OS are not supported. 
  
  
