#********************************************************************
 #                                                                 
 #  Team Edge List Mini-project: THE SHOPPING LIST HELPER
 # 
 #  This project prompts users using input() to prompt users
 #  to add (or remove) items from a shopping list. It starts empty
 #  and each time the program is run it asks you to either add or 
 #  remove an item from the list. It also updates the user of its
 #  contents. The shopping list also checks to see if an item 
 #  is already present in the list and prevents you from adding it
 #  again, giving feedback along the way. 
 # 
 # ***************************************************************/


active = True

print("Welcome to Shopping List!")
welcome_message = "Hi! I'm your shopping assistant. Can I add or remove froom you shopping list?"
print(welcome_message)

#-->Todo: declare a shopping_list list
shopping_list = ["something"]
if active == False: 
    print("Bye")
def prompt_user():
    reply = input("What do you want to add or remove?  >>  ")
    return reply
def check_answer(item):
    if item in shopping_list:
        remove_item(item)
        print(shopping_list)
    else:
        add_item(item)
        print(shopping_list)

def add_item(item):
    shopping_list.append(item)
def remove_item(item):
    shopping_list.remove(item)
while active:
    check_answer(prompt_user())