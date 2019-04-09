name = ''
while name == '':
	print ('Please enter your name: ')
	name = raw_input()
	print ('Hello ' + name + '. ' + 'Welcome to the group!!')

while True:
	print ('Please enter your password')
	password = raw_input()
	if password != 'roger':
		print ('You have typed a wrong password. Please try again.')
		continue
	print ('Access Ganted')
	break	
