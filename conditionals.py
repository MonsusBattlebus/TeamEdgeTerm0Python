
# -------------------------------------------- 
# Day 2 Challenges
# -------------------------------------------- 

message = "Welcome to Day 2.\nToday we are learning about conditionals.\nLet's practice writing some conditionals of our own!"
print(message)
# -------------------------------------------- 

print("------------------- Challenge 1 -------------------")
# Can you drive?
   # Prompt the user to enter their age.
   # Write conditional statements that print out whether you can drive in your city. 

print("Hey! How old are you?")
age = input()

if age >= 90:
   print("You probably shouldn't drive, bu you can!")
elif age >= 16:
   print("You can drive!")
elif age < 3:
   print("You're an actual baby. like, what?")
elif age < 7:
   print("You are a toddler. No.")
else:
   print("You can't drive.")








# -------------------------------------------- 

print("------------------- Challenge 2 -------------------") 

# Who placed first?
   # Write conditional statements that checks which is the highest and prints the highest score. 
   # Hint: Create three variables and assign them random scores. 

import random

score1 = random.randint(1,1000)
score2 = random.randint(1,1000)
score3 = random.randint(1,1000)
score4 = random.randint(1,1000)

if score1 > score2 and score1 > score3 and score1 > score4:
   print("Player 1 has scored the highest score of", str(score1))
elif score2 > score1 and score2 > score3 and score2 > score4:
   print("Player 2 has scored the highest score of", str(score2))
elif score3 > score1 and score3 > score2 and score3 > score4:
   print("Player 3 has scored the highest score of", str(score3))
else:
   print("Player 4 has scored the highest score of", str(score4))








# -------------------------------------------- 

print("------------------- Challenge 3 -------------------")

# One of the most common parts of our daily routine is checking the weather. 
# Our outfit and accessories are dependent on the temperature and conditions outside. 
# ie. We're probably not going to wear shorts out when it's snowing...


# **** Challenge 3: Part 1 ****
# Write a conditional statement that checks the value of the weather variable 
# and prints out a weather report based on the current weather:
# Rainy: Bring an umbrella
# Sunny: Wear a hat and sunglasses
# Snowing: Wear gloves and a scarf 

# Here's a variable to get you started:

weather = random.randint(1,3)

if weather == 1:
   weather = "Sunny"
elif weather == 2:
   weather = "Snowing"
else:
   weather = "raining"

if weather == "Sunny":
   print("It's sunny today. Make sure to wear a hat and sunglasses!")
elif weather == "Snowing":
   print("It's currently snowing. Make sure to wear gloves and a scarf")
else:
   print("It's raining right now. Remember to bring an umbrella before you go out.")
print()









# Tip: Try changing the value of the weather variable to test your other conditions.

# **** Challenge 3: Part 2 ****
# Now that you've written conditions for specific weather forecasts, let's also add in temperature! 
# You can't dress accordingly if you only know that it's raining outside but not how cold it is!
# For example:
    # If it's raining and 60 degrees, you might want to bring your umbrella and wear a light jacket.
    # However, if it's raining and 30 degrees, you might want to break out a warmer jacket with your umbrella instead. 
    
   # Add to your conditional statements above and modify your weather reports to also take into account the temperature. 
   # Make sure to account for at least three different temperatures!
   # Hint: You will need another variable to keep track of the temperature.

weather = random.randint(1,3)
temperature = 69

if weather == 1:
   weather = "Sunny"
elif weather == 2:
   weather = "Snowing"
else:
   weather = "raining"

if weather == "Sunny":
   temperatue = random.randint(70,100)
elif weather == "Snowing":
   temperatue = random.randint(-10,10)
else:
   temperatue = random.randint(40,65)

if weather == "Sunny" and weather >= 80:
   print("It's a scorching", str(temperature),"Degrees. Make sure to wear a hat, sunglasses and sunscreen!")
elif weather == "Sunny" and weather < 80: 
   print("It's gonna be a nice, warm sunny day. Remember to wear a hat and sunglasses!")
elif weather == "Snowing":
   print("It's a freezing", str(temperature), "degrees out today. Remember to wear warm clothing and make yourself a cup of hot chocolate!")
elif weather == "Raining" and temperature >= 60:
   print("It'll be rainy today at", str(temperature), "degrees. Remember an umbrella and a light jacket!")
else:
   print("It'll be rainy today at", str(temperature), "degrees. Wear a warm jacket and don't forget your umbrella!")









# -------------------------------------------- 

print("------------------- Challenge 4 -------------------")

# Prompt the user to enter the day of the week (1-7 representing Monday - Sunday)
# Write a set of conditionals that will take a number from 1 to 7 
# and print out the corresponding day of the week. 
# Make sure to add a statement that accounts for any numbers out of range! 

print("Enter the day of the week from 1-7. 1 being Sunday and 7 being Saturday.")
day = input()
day = int(day)

if day == 1:
   print("Today is Sunday. oh god here we go again.")
elif day == 2:
   print("Today is Monday. Garfield is malding.")
elif day == 3:
   print("Today is Tuesday. Ngl i kinda forget this day exists, y'know? anyways, the week just started so have fun at work/school!")
elif day == 4:
   print("It's Wednesday my dudes. AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
elif day == 5:
   print("It's Thursday! It's almost over, you can almost have fun with your life! Oh who am I kidding, you're just gonna binge Stranger Things for the 5th time this month, aren't you?")
elif day == 6:
   print("It's Friday! It's over! It's finally Over! WOOOOOOO")
elif day == 7:
   print("It's Saturday!Have fun having no idea what to do and feeling sad at like 9pm realizing you wasted your Saturday. Unless you have plans, in which have fun!")
else:
   print("Har Har. No really, what day is it?")






# -------------------------------------------- 

print("------------------- Challenge 5 -------------------")

# A leap year is a calendar year that contains an additional day added 
# to keep the calendar year synchronized with the astronomical year or seasonal year.
# To calculate if a specific year is/was a leap year, you can follow the following steps:
     # 1. If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
     # 2. If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
     # 3. If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
     # 4. The year is a leap year (it has 366 days).
     # 5. The year is not a leap year (it has 365 days).

# Those are a lot of conditions...
# Your challenge is to translate the steps above into conditionals which will evaluate if the 
# year stored in a variable is/was a leap year.

print("Hey, what year is it!?")
year = input()
year = int(year)

if year % 4 == 0:
   if year % 100 == 0:
      if year % 400 == 0:
         print ("This year's a leap year!")
      else: 
         print ("This year isn't leap year.")
   elif year % 100 != 0: 
      print ("This year's a leap year!")
else:
   print("This year isn't a leap year")