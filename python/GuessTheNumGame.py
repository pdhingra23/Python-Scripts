#This Game ask you to guess a number between 1 and 20

import random
secretNumber = random.randint(1,20)

#Ask the user to guess a number between 1 and 20
print ('I have opted a number for you. You are allowed to guess for max. 6 times')

#user will be allowed to guess six times
for GuessesTaken in range (1, 7):
	print ('Please take a guess')
	guess = int(raw_input())
	if guess > secretNumber:
		print ('Your guess is too high')
	elif guess < secretNumber:
		print ('Your guess is too low')
	elif guess == secretNumber:
        	print ('Your guess is Right. You have guessed the correct number in ' + str(GuessesTaken) + ' times!')
	else:
		break


if GuessesTaken == 6 and guess != secretNumber:
	 print ('You have exhausted you maximum number of chances. Please try again.')

#if guess == secretNumber:
#	print ('Your guess is Right. You have guessed the correct number in ' + str(GuessesTaken) + ' times!')



