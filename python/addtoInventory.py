
inv = {'gold coin':42, 'rope':1, 'dagger':5}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(dict,sample):
	total_items = 0
	for k,v in dict.items():
		total_count = 0
		if k in sample:
			total = sample.count(k) + int(v)
		else:
			total = dict[k]
		print (str(total) + ' ' + k)
		total_items = total + total_items
	print ('Total number of items: ' + str(total_items))


addToInventory(inv,dragon_loot)
