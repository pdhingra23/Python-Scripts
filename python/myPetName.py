myPets = ['howdy', 'mickey', 'zooi', 'zulu']
print ('Enter the name of the pet you are searching')
name = raw_input()
if name in myPets:
	print ('I have the pet with name: ' + name)
else:
	print ('I do not have any pet with this name')

