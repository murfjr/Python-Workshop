#testing type(var) python command

print type("hello")

print type(123)

print type(1.23)

print type(True and False) 

#now for the input

whatami=raw_input()

print type(whatami)#makes funcoutput redundant

def funcoutput(whatami):

	if type(whatami)==int:
		return "integer"
		print "integer"
	elif type(whatami)==str:
		return "string"
		print "string"
	elif type(whatami)==bool:
		return "boolean"
		print "boolean"
	elif type(whatami)==float:
		return "float"
		print "float"
funcoutput(whatami)

#defaults to "string"x

