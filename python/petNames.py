petName = []
i = 0
while True:
	print ('Enter the name of your pet ' + str(len(petName) + 1) + ' or press enter if you do not have any pet: ')
	name = raw_input()
	if name == '':
		break
	petName = petName + [name]

print ('Total number of pets you have are ' + str(len(petName)) + ' and their name are: ')

i = 1
for name in petName:
#	print (str(i) + '. ' + name)
#	i = i + 1
	print (str(petName.index(name) + 1) + '. ' + name)
