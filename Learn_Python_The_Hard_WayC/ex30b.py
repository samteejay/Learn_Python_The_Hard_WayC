#Study Drills

#Answer (1)
#Elif & Else is used to run a boolean expression that evaluates True within a block of code with multiple options

people = 40
cars = 15
buses = 30

if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."
	
if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."
	
if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."
	
if cars > people:
	print "We should take the cars."
elif buses < cars:
	print "We shouldn't take the buses."
else:
	print "Nothing."