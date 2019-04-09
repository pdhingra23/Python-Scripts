def collatz(number):
	remainder = number % 2
	if remainder == 0:
		result = number // 2
	elif remainder == 1:
		result = 3 * number + 1
	return result


print ('Please Enter your number of choice')
choice = int(input())
result = collatz(choice)
while result != 1:
	test = collatz(result)
	print(test)
	result = test
	
	
	
