# python
# Define a function called data_type, to take one argument. Compare and return results, based on the argument supplied to the function. Complete the test to produce the perfect function that accounts for all expectations.

# For strings, return its length.
# For None return string 'no value'
# For booleans return the boolean
# For integers return a string showing how it compares to hundred e.g. For 67 return 'less than 100' for 4034 return 'more than 100' or equal to 100 as the case may be
# For lists return the 3rd item, or None if it doesn't exist


def data_type(num):
	p = type(num)
	'''the argument passed will have its type passed on to the variable p, which will then be checked in the if statements below.
	The checking will be done against the data type, and action performed depending on the data type.
	'''

	if p == str:
		if len(num) == 0:
			return 'no value'
		else:
			return len(num)
	elif p == None:
		return 'no value'
	elif p == bool:
		return num
	elif p == int:
		if num < 100:
			return "less than 100"
		else:
			return "more than 100"
	elif p == list:
		if len(num) > 3:
			return num[2]
		else:
			return "None"

print data_type("Yes")
print data_type(None)
print data_type("True")
print data_type(200)
print data_type([5, 87,9,007 ])





