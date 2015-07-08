#testing type(var) python command

print type("hello")

print type(123)

print type(1.23)

print type(True and False) 

#now for the input

whatami=raw_input(">>")

def funcoutput(whatami):

	if type(whatami)==int:
		print "integer"
	elif type(whatami)==str:
		print "string"
	elif type(whatami)==bool:
		print "boolean"
	elif type(whatami)==float:
		print "float"
funcoutput(whatami)

#defaults to "string"x
