# Study Drill

def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b
	
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"

age = add(20, 4)
height = subtract(1075, 50)
weight = multiply(90, 2)
iq = float(divide(34, 100))

print "Age: %d, Height: %d, Weigth: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit,
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?\n"

# Formula for line 31 is W = 35 + 74 - 180 * (50/2)
W = 35 + 74 - 180 * (50/2)
print "Also using the normal formula: 'W = 35 + 74 - 180 * (50/2)'," 
print "The result becomes: %s" % (W)

# Try M = 24 + (34/100) - 1023. Convert it to a function.
M = add(age, subtract(height,divide(iq, 1)))
print "That becomes: %s" % M 
 
