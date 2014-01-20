# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Compensate for leap days. 
# Assume that the birthday and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 2 Jan 2012 
# you are 1 day old.
#
# Hint
# A whole year is 365 days, 366 if a leap year. 
def isLeapYear(year):
    return (year%4 == 0) and ((year%400 == 0) if ( year%100 == 0 ) else True)

def daysInMonth(year, month):
    daysInFebruary = 29 if isLeapYear(year) else 28
    daysInMonth = [31, daysInFebruary, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    return daysInMonth[month - 1]

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def dateIsAfter(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is after year2-month2-day2.  Otherwise, returns False."""
    if year1 > year2:
        return True
    if year1 == year2:
        if month1 > month2:
            return True
        if month1 == month2:
            return day1 > day2
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert dateIsAfter(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsAfter(year2, month2, day2, year1, month1, day1):
        days += 1
        (year1, month1, day1) = nextDay(year1, month1, day1)
    return days

'''
1. write a stub daysInMonth(year, month) that always returns 30
2. modify nextDay(year, month, day) to use daysInMonth(year, month)
3. test nextDay(year, month, day) using stub in daysInMonth(year, month)

4. modify daysInMonth(year, month) to be correct except for leap years
5. test nextDay(year, month, day) using stub in daysInMonth(year, month)

6. write isLeapYear(year)
7. test isLeapYear(year)
'''

def testIsLeapYear():
    years = ((1900,False), (2000,True), (1976,True), (1984,True), (2004,True), (1700,False))
    for (year, answer) in years:
            if isLeapYear(year) != answer:
                print('Test failed with year: ' + str(year))
            else:
                print('Test passed')

testIsLeapYear()
'''
8. test daysBetweenDates(...) for all test cases
'''
def testAllCases():
    print(testAllCases.__name__)
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),366),
                  ((2012,9,1,2012,9,4),3),
                  ((2013,1,1,1999,12,31), "AssertionError")]
    
    for (args, answer) in test_cases:
        try:
            result = daysBetweenDates(*args)
            if result != answer:
                print "Test with data:", args, "failed"
            else:
                print "Test case passed!"
        except AssertionError:
            if answer == "AssertionError":
                print "Nice job! Test case {0} correctly raises AssertionError!\n".format(args)
            else:
                print "Check your work! Test case {0} should not raise AssertionError!\n".format(args)
testAllCases()  # all test cases
