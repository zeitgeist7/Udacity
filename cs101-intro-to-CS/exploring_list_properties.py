# Investigating adding and appending to lists

# If you run the following four lines of codes, what are list1 and list2?

list1 = [1,2,3,4]
list2 = [1,2,3,4]

list1 = list1 + [5]
list2.append(5)

# to check, you can print them out using the print statements below.

#print list1
#print list2

'''The first list1 + [5] creates a new list and returns that while the other one (list2) still points to the same object that gets expanded to accomodate the number 5'''
'''
# Here is the proof: 

list1 = [1,2,3,4]
check = list1
list1 = list1 + [5]
print(list1)
print(check)
print(check ==  list1)

list2 = [1,2,3,4]
check = list2
list2.append(5)
print(list1)
print(check)
print(check ==  list2)
'''

# What is the difference between these two pieces of code?

def proc(mylist):
    '''
    Creates a 'new' list and appends the number 6 to the end of it
    '''
    mylist = mylist + [6]

def proc2(mylist):
    '''
    Adds 6 to the end of the list and returns the 'same' object
    '''
    mylist.append(6)

# Can you explain the results given by the four print statements below? Remove
# the hashes # and run the code to check.

list1 = [1,2,3,4]
check = list1
print(list1)
proc(list1)
print(list1)
print(check)
print(check ==  list1)

list2 = [1,2,3,4]
check = list2
print(list2)
proc2(list2)
print(list2)
print(check)
print(check ==  list2)


# Python has a special assignment syntax: +=.  Here is an example:

list3 = [1,2,3,4]
check = list3
list3 += [5]
print(list3)
print(check)
print(check ==  list3)

'''
'+=' operator behaves like listX.append(5)
'''

# Does this behave like list1 = list1 + [5] or list2.append(5)? Write a
# procedure, proc3 similar to proc and proc2, but for +=. When you've done
# that check your conclusion using the print-procedure call-print code as
# above.

def proc3(aList):
    aList += [5]

check = list3
print(list3)
proc2(list3)
print(list3)
print(check)
print(check ==  list3)

'''
'+=' keeps reference to the original list and operates on it
'''

# What happens when you try:

list1 = list1 + [7,8,9]
list2.append([7,8,9])
list3 += [7,8,9]

# When you've understood the difference between the three methods,
# write a procedure list_test which takes three lists as inputs. You should
# mutate the first input list to include 'a' as the last entry, mutate the
# second to include the entries 'a', 'b', 'c' and finally the last list should
# not be mutated but a copy should be returned with the additional entry 'w'.

def list_test(first, second, third):
    first.append('a')
    second += ['a', 'b', 'c']
    third = third + ['w']

    return third



first_input = [1,2,3]
second_input = [4,5,6]
third_input = [7,8,9]

print list_test(first_input, second_input, third_input)
#>>> [7,8,9,'w']
print first_input
#>>> [1,2,3,'a']
print second_input
#>>> [4,5,6,'a','b','c']
print third_input
#>>> [7,8,9]
