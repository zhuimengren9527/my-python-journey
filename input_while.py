# ~ message = input("Tell me something,and I will repeat it back to you:")
# ~ print(message)

# ~ name = input("Please enter your name:")
# ~ print("f\nHello,{name}")

# ~ prompt ="If you share your name,We can personalize the message you see."
# ~ prompt += "\nWhat's your first name? "

# ~ name = input(prompt)
# ~ print(f"\nHello,{name}")
 
# ~ height = input("How tall are you,in inches? ")
# ~ height = int(height)

# ~ if height >= 48:
    # ~ print(f"\nYou are tall enough to ride!")
# ~ else:
    # ~ print(f"You'll be able to ride,When you are a little older")
    
# ~ number =input("Enter a number,and I'll tell you it's even or odd:")
# ~ number = int(number)

# ~ if number % 2 == 0:
    # ~ print(f"\nThe number {number} is even")
# ~ else:
    # ~ print(f"\nThe number {number} is odd")

# ~ attendance = input("How many people in your party? ")
# ~ attendance = int(attendance)

# ~ if attendance > 8:
    # ~ print(f"\nSorry there are no tables available!")
# ~ else:
    # ~ print(f"\\nYes,We have a table available!")

# ~ number = input("Please enter a number! ")
# ~ number = int(number)

# ~ if number % 10 == 0:
    # ~ print(f"\n{number}是10的整数倍")
# ~ else:
    # ~ print(f"\n{number}不是10的整数倍")

# ~ prompt ="\nTell me something,and I will repeat ti back to you!"
# ~ prompt += "\nEnter quit to end the program."

# ~ message = ""
# ~ while message != 'quit':
    # ~ message = input(prompt)
    
    # ~ if message != 'quit':
        # ~ print(message)

# ~ #   标志flag
# ~ prompt ="\nTell me something,and I will repeat ti back to you!"
# ~ prompt += "\nEnter quit to end the program."

# ~ active = True
# ~ while active:
    # ~ message = input(prompt)
    
    # ~ if message == 'quite':
        # ~ active = false
    # ~ else:
        # ~ print(message)

# ~ #   使用break退出循环
# ~ prompt ="\nTell me something,and I will repeat ti back to you!"
# ~ prompt += "\nEnter quit to end the program."

# ~ while True:
    # ~ message = input(prompt)
    
    # ~ if message == 'quit':
        # ~ break
    # ~ else:
        # ~ print(message)
        
# ~ #   在循环中使用continue
# ~ current_number = 0
# ~ while current_number < 10:
    # ~ current_number += 1
    # ~ if current_number % 2 == 0:
        # ~ continue
    # ~ else:
        # ~ print(current_number)

#   练习1
# ~ prompt = "Please enter the toppings you want on your pizza! "

# ~ message = ""
# ~ while message != 'quit':
    # ~ message = input(prompt)
    
    # ~ if message == 'quit':
        # ~ break
    # ~ else:
        # ~ print(f"\nAdd the {message}")
    
# ~ #   练习2
# ~ prompt = "How old are you?  "


# ~ active = True
# ~ while active:
    
    # ~ age = input(prompt)
    
    # ~ if age == 'quit':
        # ~ active = False
    
    # ~ else:
        # ~ age = int(age)
        
        # ~ if age < 3:
            # ~ print(f"\nfree!!!")
        # ~ elif age < 12:
            # ~ print(f"\nEach ticket is 10 dollars.")
        # ~ else:
            # ~ print(f"\nEach ticket is 15 dollars.")
        
# ~ #   无限循环
# ~ x = 1
# ~ while x > 0:
   
    # ~ print(x)
    
#   练习3
# ~ prompt = "请输入书名："

# ~ message = ""
# ~ active = True
# ~ count = 0
# ~ while active:
    # ~ message = input(prompt)
    
    # ~ if message == 'quit':
        # ~ print("程序已退出")
        # ~ break
    # ~ elif message == '':
        # ~ print("请输入书名！")
        # ~ continue
    # ~ else:
        # ~ print(f"已借：{message}")
        # ~ count += 1
        
    # ~ if count >5:
        # ~ print("借书已达到上限")
        # ~ break
    
 # ~ #  列表之间移动元素
# ~ unconfirmed_users = ['alice','brian','cadace']
# ~ confirmed_users = []
 
# ~ while unconfirmed_users:
    # ~ current_user = unconfirmed_users.pop()
     
    # ~ print(f"\nVerifying user : {current_user}")
    # ~ confirmed_users.append(current_user)
     
# ~ print(f"\nThe following users have been confirmed:")
# ~ for confirmed_user in confirmed_users:
    # ~ print(f"\n{confirmed_user.title()}")

# ~ # 使用用户输入填充字典
# ~ responses = {}
# ~ polling_active = True

# ~ while polling_active:
    # ~ name = input("\nWhat is your name?")
    # ~ response = input("\nWhich mountain would you like to climb someday?")
    
    # ~ responses[name] = response
    
    # ~ repeat = input("Would you like to let another person respond?(yes/no)")
    # ~ if repeat == 'no':
        # ~ polling_active = False
# ~ print("\n---Poll Results---")
# ~ for name,response in responses.items():
    # ~ print(f"\n{name} would like to climb {response}.")
    

# ~ # 练习1
# ~ sandwiches_orders = ["ham sandwich", "chicken sandwich", "veggie sandwich"]
# ~ finished_sandwiches = []

# ~ while sandwiches_orders:
    
    # ~ sandwich = sandwiches_orders.pop()
    # ~ print(f"\nI made your {sandwich} sandwich.")
    # ~ finished_sandwiches.append(sandwich)

# ~ for sandwich in finished_sandwiches:
    # ~ print(f"\n{sandwich}")

# ~ #   练习2
# ~ sandwiches_orders = ["ham sandwich", "pastrami","chicken sandwich","pastrami","veggie sandwich","pastrami","pastrami"]
# ~ print(f"'pastrami'已经卖完了！")
# ~ active = True
# ~ while 'pastrami' in sandwiches_orders:
     
        # ~ sandwiches_orders.remove('pastrami')
        
# ~ print(f"\n{sandwiches_orders}")
        
#   练习3
responses = {}
active = True

while active:
    name = input("\nWhat is your name? ")
    if name == '':
        break
    
    response = input("If you could visit one place in the world, where would you go? ")
    if response == '':
        break
    
    responses[name] = response

print("\n---Results---")
for name, response in responses.items():
    print(f"{name} would like to visit {response}.")
    

    













