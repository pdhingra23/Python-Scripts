stuff = {'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6, 'dagger': 1}


def displayInventory(sample):
	print ('Inventory:')
	total_items = 0
	for k, v in sample.items():
		print (str(v) + ' ' + k)
		total_items = total_items + v
	print ('Total number of items: ' + str(total_items))


displayInventory(stuff)
