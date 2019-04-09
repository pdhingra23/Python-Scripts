name = ''
while name == '':
	print ('Please enter your name: ')
	name = raw_input()
	print ('Hello ' + name + '. ' + 'what is the password?')
	password = raw_input()
	if password != 'swordfish':
		print ('You have typed a wrong password. Please try again.')
		break
	print ('Access Ganted')
