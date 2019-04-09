def comma(listtest):
#	print (listtest[0:(len(listtest) - 1)], end =" ")
#	print ('and ' + listtest[(len(listtest) - 1)])
	x = listtest[0:(len(listtest) - 1)]
	y = listtest[(len(listtest) - 1)]
	z = ', '
	print (z.join(x) + ' and ' + y)



spam = ['apples', 'bananas', 'tofu', 'orange']
comma(spam)


#we want output like this ==> 'apples, bananas, tofu and orange'


# x = listtest[0:(len(listtest) - 1)]
# y = listtest[(len(listtest) - 1)]
# z = ', '
# print (z.join(x) + 'and' + y)
 
