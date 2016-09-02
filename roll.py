#!/usr/bin/python
import random
print "Welcome to dice roller for d&d. Choose the die you want to roll."

while True:
	print "\n 1. 1d4 \n 2. 1d6 \n 3. 1d8 \n 4. 1d10 \n 5. 1d12 \n 6. 1d20 \n"
	choice = raw_input("Enter a number, or q to quit.\n")
	if choice == 'q':
		break
	elif choice.isdigit() == False:
		print "Invalid Input."
		break
	choice = int(choice)
	if choice == 1:
		print "You rolled a {}.".format(random.randrange(1,5))
	elif choice == 2:
		print "You rolled a {}.".format(random.randrange(1,7))
	elif choice == 3:
		print "You rolled a {}.".format(random.randrange(1,9))
	elif choice == 4:
		print "You rolled a {}.".format(random.randrange(1,11))
	elif choice == 5:
		print "You rolled a {}.".format(random.randrange(1,13))
	elif choice == 6:
		print "You rolled a {}.".format(random.randrange(1,21))
	else:
		print "Invalid input."

