#-------------------------------------------------------------------------------------------------
# Grant De La Campa
# @2019
# dateValidation.py
# function: Calculates leap years and determines the number of days in a month based on the year.
#--------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------
#           GLOBALS
#---------------------------------------------------------------------------------

type1 = [1, 3, 5, 7, 8, 10, 12]
type2 = [4, 6, 9, 11]

#---------------------------------------------------------------------------------
#           CONSTRAINT FUNCTIONS
#---------------------------------------------------------------------------------


def leapYearCheck(year):
    if((year % 4 == 0) & (year % 100 != 0)) | (year % 400 == 0):
        return True
    else:
        return False

def dayConstraint(year, month):
    isLeap = leapYearCheck(year)
    if month in type1:
        return 31
    elif month in type2:
        return 30
    else:
        if(isLeap):
            return 29
        else:
            return 28
