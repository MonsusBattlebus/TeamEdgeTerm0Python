
# -------------------------------------------- 

	# You've just learned about functions.
	# Functions are reusable pieces of code that make your code more modular.
	
	# If you are writing the same bit of code over and over, you are doing more work that you have to.
	# Use functions to simplify your code and decrease the amount of work you're doing. 

	# Any time you start thinking 'this is tedious', you can probably write a function for that task.

# -------------------------------------------- 


# -------------------------------------------- 
  # Challenge 1: Let's try to write some basic functions.
# -------------------------------------------- 


print("------------------- Challenge 1 -------------------")

# **** Challenge 1: Problem 1 ****
# Write a function called print_message() that prints any message you want.

def print_message(message):
	print(message)

# **** Challenge 1: Problem 2 ****
# Write a function called print_five_messages() that calls print_message() five times.

def print_five_messages(message):
	for x in "sussy":
		print_message(message)

# **** Challenge 1: Problem 3 ****
# Write a function called get_user_input() that asks the user if they'd like to print your message
# once or five times. Then call one of the two functions above based on what the user decides.

def get_user_input(message):
	print("How many times would you like to print the message. One or Five?")
	times = str(input())
	if times == "Five" or times == "five":
		print_five_messages(message)
	elif times == "One" or times == "one":
		print_message(message)
	else:
		print ("Please put 1 or 5. Not spelled out")

# **** Challenge 1: Problem 4 ****
# Write a function called print_greeting() that prints a greeting message to the user.

def print_greeting():
	print("Welcome!")

# **** Challenge 1: Problem 5 ****
# Write a function called print_closing() that prints a goodbye message to the user.

def print_closing():
	print("Goodbye. I hope you enjoyed this program.")

# **** Challenge 1: Problem 6 ****
# Write a function called run() that greets the user, asks them for input, and sends a goodbye message.
# Remember! Use the functions that you've already made. Don't hardcode anything!

def run():
	print_greeting()
	print("Please input something")
	user_input = input()
	print_closing()

# -------------------------------------------- 

# Challenge 2: Functions are also able to take input and return output. 
				# The value(s) you pass to it are called parameters.

# -------------------------------------------- 

print("------------------- Challenge 2 -------------------")

# **** Challenge 2: Problem 1 ****

# Write a function called sum_double that takes two number paramters and returns their sum.
# However, if the two values are the same, the funciton will return double their sum.

	# Examples:
		# sum_double(1, 2) → 3
		# sum_double(3, 2) → 5
		# sum_double(2, 2) → 8

# -------------------------------------------- 

def sum_double(x,y):
	if x == y:
		print((x+y)*2)
	elif x != y:
		print (x+y)
	else:
		print("ERROR")

print_message(input())
print_five_messages(input())
get_user_input(input())
print_greeting()
print_closing()
run()


# Make sure to test your code! Write a few function calls to make sure your code works!

# -------------------------------------------- 

# **** Challenge 2: Problem 2 ****

# Write a function called makes_10 that takes two numbers, a and b, and returns true if one of them is 10 or if their sum is 10.

	# Examples:
		# makes_10(9, 10) → True
		# makes_10(9, 9) → False
		# makes_10(1, 9) → True

# -------------------------------------------- 


def makes_10(a,b):
	answer = False
	if a == 10 or b == 10 or a + b == 10:
		answer = True
		return answer
	else:
		answer = False
		return answer

print("makes_10 test")
print(makes_10(8,2))


# Make sure to test your code! Write a few function calls to make sure your code works!

# -------------------------------------------- 

# **** Challenge 2: Problem 3 ****

# Write a function that will return the time our alarm is set to go off.

# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean
# indicating if we are on vacation, return a string in the form "7:00" indicating
# when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on
# the weekend it should be "10:00". However, if we are on vacation -- then on weekdays
# it should be "10:00" and weekends it should be "off".
	# Examples:
		# alarm_clock(1, False) → "7:00"
		# alarm_clock(6, True) → "off"
		# alarm_clock(0, False) → "10:00"

# -------------------------------------------- 

def alarm_clock(x, y):
	alarm = "7:00"
	if x == 0 and y == True or x == 6 and y == True:
		alarm = "Off"
		return alarm
	elif x == 0 and y == False or x == 6 and y == False:
		alarm = "10:00"
		return alarm
	elif x > 0 and x < 6 and y == True:
		alarm = "10:00"
		return alarm
	elif x > 0 and x < 6 and y == False:
		alarm = "7:00"
		return alarm



print (alarm_clock(0, False))
print (alarm_clock(6, True))
print (alarm_clock(1, False))
print (alarm_clock(1, True))

# Make sure to test your code! Write a few function calls to make sure your code works!

# -------------------------------------------- 

# **** Challenge 2: Problem 4 ****

# Write a function that will tell you if you received a speeding ticket.
# You are driving a little too fast, and a police officer stops you. 

# To compute the result, encoded as a number value: 
	# 0=no ticket
	# 1=small ticket
	# 2=big ticket
# If speed is 60 or less, the result is 0. 
# If speed is between 61 and 80 inclusive, the result is 1. 
# If speed is 81 or more, the result is 2.

# -------------------------------------------- 


def ticket_cost(s):
	result = 0
	if s <= 60:
		result = 0
		return result
	elif s > 60 and s <= 80:
		result = 1
		return result
	elif s >= 81:
		result = 2
		return result

print(ticket_cost(50))
print(ticket_cost(70))
print(ticket_cost(90))






# Make sure to test your code! Write a few function calls to make sure your code works!
