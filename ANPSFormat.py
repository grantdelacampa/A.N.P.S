#---------------------------------------------------------------------
# Grant De La Campa
# @2019
# ANPSFormat.py
# Functions:
#---------------------------------------------------------------------
    # breaks visual flow hence breakpoint
def breakpoint(message):
    print("--------------------------------------------------------------------------------")
    print("          ", message)
    print("--------------------------------------------------------------------------------")

    # Generic error message for input loops
def eHandler(error):
    print("ERROR: ", error, " is not valid")
def listPrint(itemList):
    for item in itemList:
        print("    -", item)
    # Formatted list printer for menu option calls
def listCalls(callList):
    calls = "     -Calls: "
    for item in callList:
        calls = calls + item + " "
    print(calls)
    print("--------------------------------------------------------------------------------")
