#############################################################################
 #                                                                  
 #  Team Edge dictionaries: Dictionaries CHALLENGES 
 # 
 #  For this activity, you will be building a dictionary and with properties
 #  and methods. You will access the properties, set new values, and use
 #  the methods to change your dictionary state. What dictionary? Ask your coach.
 # 
 #  1. DEFINE: Make a dictionary and set its properties, printing changes in between.
 #  2. MODIFY: Add 2 new properties and assing values. Change existing values,
 #     including adding or updating values inside lists
 #  3. METHODS: Now its time to make some methods tha can make a change
 #     to your values, like a boolean, or they can print something about
 #     the dictionary. Nothing fancy, unless you fancy it.
 #  4. LITERALLY: Use string literals to put it all together in one statement.
 # 
 # #########################################################################/

from imghdr import what


print("------------------- CHALLENGE 1 : DEFINE    -------------------")

#Below is a simple example of a dictionary implementaion. 
#-->TODO: Add at least 3 comments to the dictionary below to demonstrate you understand its usage

dictionary = {
    "name": "box",
    "sus": True,
    "sussy": "baka",
    "Persona": "SSS+-Tier",
    "is_empty": True
}
#working with the dictionary:
dictionary["length"] = 12
dictionary["width"] = 8
dictionary["contents"] = ["thing 1", "thing 2", "thing 3"]
print(f"{dictionary['name']} is {dictionary['length']} {dictionary['width']}")
dictionary["contents"].append("thing 4")
print(f"{dictionary['name']} has {dictionary['contents']}")
print(dictionary)

 

#-->TODO: Declare a new dictionary and set at least 4 properties to it including: string, boolean, number, list

new_dict = {
    "Naruto": "Mid",
    "Average Age of a Naruto Fan": -5,
    "Saiki K best anime?": True,
    "What Naruto Fans do": ["Cope","Mald","Seethe"]
}

##################################  MY dictionary ########################### #/

print(new_dict["What Naruto Fans do"])




########################################################################## #/



print("------------------- CHALLENGE 2 : MODIFY   -------------------")

#-->TODO: Print your dictionary you created above

print(new_dict)

#-->TODO: Update the dictionary you just created  by adding new properties and values, including list elements, in this section.

new_dict["The Island"] = "The Island is going to blow up in 8 minutes"
new_dict["Lmao"] = "You blue gumball son of a bitch and you hot topic wannabe"
new_dict["I hate you"] = "You have done nothing but ruin my life I hope you both die."

#-->TODO: Print your dictionary again and observe changes

print(new_dict)

print("------------------- CHALLENGE 3 : MEHTODS   -------------------")


#-->TODO: Make a method that will update your dictionary value. It should take in a dictionary and return it modified.

def mogus(Thing_they_want_changed,what_to):
    new_dict[Thing_they_want_changed] = what_to

#-->TODO: Call the method.

mogus("Lmao","Sussy Baka")

print("------------------- CHALLENGE 4 : LITERALLY   -------------------")

#-->TODO: Put it all together using a string literal to tell the story of your dictionary!

def stringlit(dict):
    stringlit = ""
    for x,y in dict.items():
        stringlit += str(x) + ","
        stringlit += str(y) + ","
    return stringlit

print(stringlit(new_dict))