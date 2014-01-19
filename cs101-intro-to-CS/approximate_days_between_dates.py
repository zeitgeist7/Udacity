# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct ouptuts yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def equalDates(date1, date2):
	return (date1[0] == date2[0]) and (date1[1] == date2[1]) and (date1[2] == date2[2])
        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
        
    # YOUR CODE HERE!
    date1 = (year1, month1, day1)
    date2 = (year2, month2, day2)
    dayCount = 0
    while (not equalDates(date1, date2)):
    	date1 = nextDay(date1[0], date1[1], date1[2])
    	dayCount += 1
    return dayCount

def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
            print ("Number calculated: " + str(result))
        else:
            print "Test case passed!"

test()
    
