# ~ cars=['audi','bmw','subaru','toyota']
# ~ for car in cars:
    # ~ if car=='bmw':
        # ~ print(car.upper())
    # ~ else:
        # ~ print(car.title())

# ~ aline_color='green'
# ~ if aline_color=='green':
    # ~ print("The player has obtainde 5 points")
# ~ if aline_color=='red':
    # ~ print("The player has obtainde 5 points")

# ~ aline_color='green'
# ~ if aline_color=='red':
    # ~ print("The player has obtained 5 points by annihilating the aliens")
# ~ else:
    # ~ print("The player has obtained 10 points")

# ~ aline_color='red'
# ~ if aline_color=='green':
    # ~ print("The player has obtained 5 points")
# ~ elif aline_color=='yellow':
    
    # ~ print("The player has obtained 10 points")
# ~ elif aline_color=='red':
    
    # ~ print("The player has obtained 15 points")

# ~ requested_toppings = ['mushrooms','green peppers','extra cheese']
# ~ for requested_topping in requested_toppings:
    # ~ if requested_topping=='green peppers':
        # ~ print("Sorry,we are out of green peppers right now")
    # ~ else:
        # ~ print(f"Adding {requested_topping}.")
# ~ print(f"\nFinished making your pizza!")

available_toppings = ('mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese')
requested_toppings = ['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_toppings}.")
    else:
        print(f"Sorry,we don't have {requested_topping}.")
print(f"\nFinished making your pizza!")
