menu = {
    'pizza' : '$5',
    'hamburger' : '$8',
    'cheese' : '$10'
}

for food in menu:
    food_cost = menu.get(food)
    print(food, food_cost)

user_input = input("What food would you like? ").lower().strip()

check_menu = menu.get(user_input)

if check_menu == None:
    print("Sorry thats not on the menu...")
else:
    print(check_menu)