# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(elements):
	if not elements:
		return None
	highestFrequencyElement = previousElement = elements[0]
	highestCount = currentCount = 0

	for i in xrange(len(elements)):
		if elements[i] == previousElement:
			currentCount = currentCount + 1
		else:
			if currentCount > highestCount:
				highestCount = currentCount
				currentCount = 1
				highestFrequencyElement = previousElement
		previousElement = elements[i]

	if currentCount > highestCount:
		highestFrequencyElement = elements[-1]
	return highestFrequencyElement


#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None

print longest_repetition([2, 2, 3, 3, 3])
# 3
