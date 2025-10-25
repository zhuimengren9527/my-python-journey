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
# ~ responses = {}
# ~ active = True

# ~ while active:
    # ~ name = input("\nWhat is your name? ")
    # ~ if name == '':
        # ~ break
    
    # ~ response = input("If you could visit one place in the world, where would you go? ")
    # ~ if response == '':
        # ~ break
    
    # ~ responses[name] = response

# ~ print("\n---Results---")
# ~ for name, response in responses.items():
    # ~ print(f"{name} would like to visit {response}.")
    
# ~ #   练习4
# ~ books = ['小王子','三体','活着','骆驼祥子','伦理学']

# ~ borrowed_books = []
# ~ empty_count = 0
# ~ while  True:
    # ~ prompt = input("请输入书名: (输入quit结束)")
    
    # ~ if prompt == 'quit':
        # ~ break
    
    # ~ elif prompt == "":
        # ~ empty_count += 1
        # ~ if empty_count >=3:
            # ~ print ("检测到连续三次空输入，系统已退出。")
            # ~ break
         
         
            
        # ~ print('请输入有效书名！')
        # ~ continue
  
    # ~ elif prompt in books:
        # ~ books.remove(prompt)
        # ~ borrowed_books.append(prompt)
        # ~ print(f"\n已借出：《{prompt}》")
    # ~ else:
          # ~ print(f"\n未找到《{prompt},请确认书名》")  
                
# ~ if borrowed_books:
    # ~ print("\n您已借阅以下书籍： ")
    # ~ for book in borrowed_books:
        # ~ print(f"- 《{book}》")
# ~ else:
    # ~ print("\n您未借阅任何书籍。")

# ~ # 练习5
# ~ inventory = ['可乐','薯片','牛奶','苹果','啤酒','花生','瓜子']

# ~ shopping_trolly = []

# ~ goods_number = 0
# ~ empty = 0
# ~ while True:
    # ~ prompt = input("\n请输入要购买的商品： ")
    
    # ~ if prompt =="":
        # ~ empty += 1
        # ~ if empty >3:
            # ~ print("\n未输入商品，系统已退出！")
            # ~ break
        # ~ else:
            # ~ print("\n请输入有效商品！")
    # ~ elif prompt == 'quit':
        # ~ break
        
        
    # ~ elif prompt in inventory:
        # ~ goods_number += 1
        # ~ if goods_number > 5:
            # ~ print("\n购物已达上限！")
            # ~ break
        # ~ else:
            # ~ shopping_trolly.append(prompt)
            # ~ print("\n已加入购物车")
            # ~ continue
    # ~ else:
        # ~ print("\n抱歉，暂时缺货！")
        
# ~ if shopping_trolly:
    
    # ~ print(f"\n你已购买以下商品：")
    # ~ for commodity in shopping_trolly:
        # ~ print(f"- {commodity}")
    
# 练习6
# ~ pets_available = ['狗','猫','兔子','鹦鹉','仓鼠']
# ~ adopted_pets = []

# ~ empty = 0
# ~ while True:
    # ~ prompt = input("\n请输入你想领养的宠物（输入quit退出系统）： ").strip()
    # ~ if prompt == "":
        # ~ empty += 1
        # ~ if empty >3:
            # ~ break
        # ~ else:
            # ~ print(f"\n如果你喜欢Enter，不如把他扣下来吃掉！")
            # ~ continue
    # ~ elif prompt.lower() == 'quit':
        # ~ break
    # ~ elif prompt in pets_available:
        # ~ pets_available.remove(prompt)
        # ~ adopted_pets.append(prompt)
        # ~ print("\n你想领养的宠物已登记")
        # ~ empty = 0
        # ~ continue
    # ~ else:
        # ~ print(f"\n我这里没有，你自己生一个吧！")
# ~ if adopted_pets:
    # ~ print("\n请到现场来付保释金并提走你心爱的捣蛋鬼: ")
    # ~ for pet in adopted_pets:
        # ~ print(f"\n- {pet}")

# ~ # 练习7
# ~ pets = {'狗':5,'猫':3,'大象':6,'老虎':10,'鳄鱼':5,'狮子':9}
# ~ adopted_pets = {}
# ~ empty = 0
# ~ while True:
    # ~ pet_name = input(f"\n请输入你想领养的宠物名: ").strip()
   
    # ~ if pet_name == "":
        # ~ empty += 1
        # ~ if empty >3:
            # ~ print(f"\n未输入宠物名字，系统已自动退出！")
            # ~ break
       
    # ~ elif pet_name == "quit":
        # ~ break
    
    # ~ elif pet_name in pets:
        # ~ pet_amount = input(f"\n请输入领养数量： ")
        
        
        # ~ try:
            # ~ pet_amount = int(pet_amount)
        # ~ except ValueError:
            # ~ print(f"\n请输入有效数字！")
            # ~ continue
            
        
        # ~ if pet_amount > pets[pet_name]:
            # ~ print(f"\n超出最高领养数量！")
            # ~ continue
        # ~ else:
            # ~ pets[pet_name] -= pet_amount
            # ~ adopted_pets[pet_name] = (
            # ~ adopted_pets.get(pet_name,0) + pet_amount
            # ~ )
            # ~ if pets[pet_name] == 0:
                # ~ print(f"\n已售罄，请选择别的宠物！！")
                # ~ continue
            # ~ continue_adoption = input(f"\n请问是否继续选择领养(请输入是或否)：")
            # ~ continue_adoption = continue_adoption == '是'
            
            # ~ if  continue_adoption:
               # ~ continue
            # ~ else:
                # ~ break
            
   
# ~ if adopted_pets:
    # ~ print("\n你的宠物清单如下： ")
    # ~ for pet_name,pet_amount in adopted_pets.items():
        # ~ print(f"\n- {pet_name}:{pet_amount}只。")
# ~ # 练习8
# ~ fruits = {
    # ~ '苹果': {'库存':10, '单价':3.5, '产地':'山东'},
    # ~ '香蕉': {'库存':15, '单价':2.2, '产地':'云南'},
    # ~ '橙子': {'库存':20, '单价':4.0, '产地':'四川'},
    # ~ '西瓜': {'库存':5,  '单价':12.0, '产地':'甘肃'},
    # ~ '葡萄': {'库存':8,  '单价':6.5, '产地':'新疆'},
    # ~ '草莓': {'库存':12, '单价':8.0, '产地':'辽宁'}
# ~ }
# ~ shopping_trolley = {}
# ~ empty = 0 
# ~ for fruit_name,fruit_attributes in fruits.items():
    # ~ print(f"\n{fruit_attributes}")
# ~ while True:
    # ~ fruit_customer = input(f"\n请选择需要购买的水果： ")
    # ~ if fruit_customer == "":
        # ~ empty += 1
        # ~ if empty > 3:
            # ~ print(f"\n未输入水果名称，系统已退出")
            # ~ break
    # ~ if fruit_customer == 'quit':
        # ~ break
        
       
            
    
    # ~ if fruit_customer in fruits:
        # ~ fruit_attributes = fruits[fruit_customer]
        # ~ buy_amount = input(f"\n请输入购买数量： ")
        # ~ try:
            # ~ buy_amount = int(buy_amount)
        # ~ except ValueError:
            # ~ print(f"\n请输入有效数字！")
            # ~ continue
        
        # ~ if buy_amount > fruit_attributes['库存']:
            # ~ print(f"\n该水果已超过购买上限，请重新选择")
            # ~ continue
        # ~ else:
            # ~ fruit_attributes['库存'] -= buy_amount
            # ~ shopping_trolley[fruit_customer] = shopping_trolley.get(fruit_customer,0) + buy_amount
            # ~ continue_buy = input(f"\n你选择的水果已加入购物车，是否继续购买（是/否）: ")
            # ~ continue_buy = continue_buy == '是'
            # ~ if continue_buy:
                # ~ continue
            # ~ else:
                # ~ break

# ~ if shopping_trolley:
    # ~ print(f"\n你已购买以下水果：")
    # ~ for fruit_name, quantity in shopping_trolley.items():
        # ~ unit_price = fruits[fruit_name]['单价']
        # ~ producing_area = fruits[fruit_name]['产地']
        # ~ total_price = quantity * unit_price
        # ~ print(f"- {fruit_name}：{quantity}只，单价{unit_price}元，总价{total_price}元，产地{producing_area}")
        
# ~ #   练习9
# ~ countries = {
    # ~ '中国': {'首都': '北京', '人口': '14亿', '面积': '960万平方公里'},
    # ~ '美国': {'首都': '华盛顿', '人口': '3亿', '面积': '983万平方公里'},
    # ~ '印度': {'首都': '新德里', '人口': '13亿', '面积': '328万平方公里'},
    # ~ '法国': {'首都': '巴黎', '人口': '6700万', '面积': '64万平方公里'}
# ~ }
# ~ for country_name,country_attribute in countries.items():
    # ~ print(f"\n{country_name}")
    # ~ print(f"{country_name}:{country_attribute['首都']}:{country_attribute['人口']}")
# ~ empty = 0
# ~ while True:
    # ~ users_info = input(f"\n请输入你要查询的国家： ")
    # ~ if users_info == '':
        # ~ empty +=1
        # ~ if empty > 3:
            # ~ print(f"\n你未输入任何有效信息，系统已退出！！！")
            # ~ break 
    # ~ elif users_info == 'quit':
        # ~ break
    # ~ elif users_info in countries:
        # ~ print(f"\n{users_info}:{country_attribute['首都']}:{country_attribute['人口']}:{country_attribute['面积']}")
        # ~ empty = 0
    # ~ else:
        # ~ print(f"\n该国家不存在 ")

#   练习10
# ~ merchandise = {
    # ~ '苹果': {'价格': 3.5, '库存': 10, '折扣': 0.9},
    # ~ '香蕉': {'价格': 2.2, '库存': 15, '折扣': 1.0},
    # ~ '橙子': {'价格': 4.0, '库存': 20, '折扣': 0.85},
    # ~ '西瓜': {'价格': 12.0, '库存': 5, '折扣': 0.8},
    # ~ '葡萄': {'价格': 6.5, '库存': 8, '折扣': 0.95}
# ~ }
# ~ shopping_trally = {}
# ~ empty = 0
# ~ print(f"\n可供选择的商品如下： ")
# ~ for merchandise_name,merchandise_attribute in merchandise.items():
    # ~ print(f"\n-{merchandise_name}:'价格' {merchandise_attribute['价格']} '库存'{merchandise_attribute['库存']} '折扣'{merchandise_attribute['折扣']}")
# ~ while True:
    # ~ customer_info = input(f"\n请输入你想购买的商品： ")
    # ~ if customer_info == '':
        # ~ empty += 1
        # ~ if empty > 3:
            # ~ print(f"\n未输入有效商品，系统已自动退出！！！")
            # ~ break 
    # ~ elif customer_info == 'quit':
        # ~ confirm_info = input(f"\n你确定要退出吗？(是/否)：")
        # ~ confirm_info = confirm_info == '是'
        # ~ if confirm_info:
            # ~ break
        # ~ else:
            # ~ continue
    # ~ if customer_info in merchandise:
        # ~ purchase_quality = input(f"\n请输入你要购买的数量")
        
        # ~ try:
            # ~ purchase_quality = int(purchase_quality)
        # ~ except ValueError:
            # ~ print(f"\n请输入有效数量！！！")
            # ~ continue
        # ~ if purchase_quality > merchandise_attribute['库存']:
            # ~ print(f"\n库存不足，请重新输入： ")
            # ~ continue 
        # ~ merchandise_attribute['库存'] -= purchase_quality
    
        # ~ if customer_info in shopping_trally:
            # ~ shopping_trally[customer_info]['数量'] += purchase_quality
        
        # ~ else:
             # ~ shopping_trally[customer_info] = {
                # ~ '价格': merchandise_attribute['价格'],
                # ~ '数量': purchase_quality,
                # ~ '折扣': merchandise_attribute['折扣']
            # ~ }
        
        # ~ continue_info = input(f"\n你选购的商品已加入购物车，请问是否继续购买(是/否)： ").strip()
        # ~ if continue_info != '是':
            # ~ break
    # ~ else:
        # ~ print(f"\n请输入正确的商品名称")
        
# ~ if shopping_trally:
    # ~ total_price = 0
    # ~ print(f"\n你购买的商品如下：")
    # ~ for product_name, details in shopping_trally.items():
        # ~ unit_price = details['价格']
        # ~ quantity = details['数量']
        # ~ discount = details['折扣']
        # ~ product_total_price = unit_price * quantity * discount
        # ~ total_price += product_total_price
        # ~ print(f"- {product_name}: 单价 {unit_price} 元，数量 {quantity}，折扣 {discount * 100}%，总价 {product_total_price:.2f} 元")

    # ~ print(f"\n购物车总价（折扣后）：{total_price:.2f} 元")
# ~ else:
    # ~ print("购物车为空，感谢光临！")
    
# ~ #   练习11
# ~ library = {
    # ~ 'Python编程': {'作者': '李明', '库存': 10, '价格': 50},
    # ~ '数据结构与算法': {'作者': '王辉', '库存': 5, '价格': 80},
    # ~ '机器学习': {'作者': '张磊', '库存': 8, '价格': 120},
    # ~ '深入Python': {'作者': '赵刚', '库存': 3, '价格': 100},
    # ~ '人工智能导论': {'作者': '刘敏', '库存': 6, '价格': 150}
# ~ }

# ~ book_trally = {}
# ~ empty = 0
# ~ while True:
    
    # ~ user_check = input(f"\n请输入'查询'查看当前书目： ")  
    # ~ if user_check  !='查询':
        # ~ continue
    # ~ else:
        # ~ for book_name,book_attribute in library.items():
            # ~ print(f"\n{book_name}:{book_attribute}")
            
    # ~ book_choosed = input(f"\n请输入需要借阅的图书： ")
    # ~ if book_choosed == '':
        # ~ empty += 1
        # ~ if empty > 3:
            # ~ print(f"\n未输入有效书名，系统已退出！！！！")
            # ~ break
    # ~ elif book_choosed == 'quit':
        # ~ break
    
   
   
    # ~ if book_choosed in library:
        # ~ book_amount = input(f"\n请输入需要借阅的数量：")
        
        # ~ try:
            # ~ book_amount = int(book_amount)
        # ~ except ValueError:
            # ~ print(f"\n请输入有效数字！！！")
            # ~ continue
            
        # ~ if book_amount > book_attribute['库存']:
            # ~ print(f"\n超出库存，请重新输入！！！")
            # ~ continue
            
        # ~ library[book_choosed]['库存'] -= book_amount    
            
        # ~ if book_choosed in book_trally:
            # ~ book_trally[book_choosed]['库存'] += book_amount
        # ~ else:
            # ~ book_trally[book_choosed] = {'作者':library[book_choosed]['作者'],'库存':book_amount,'价格':library[book_choosed]['价格']}
            # ~ continue_borrow = input(f"\n你选择的图书已加入购物车,是\否j继续借阅： ")
            
            # ~ if continue_borrow != '是':
                # ~ break
            # ~ else:
                # ~ continue
    # ~ else:
        # ~ print(f"\n该书不存在，请重新输入！！！")
        # ~ continue
# ~ if book_trally:
    # ~ print(f"\n你借阅的书籍如下： ")
    # ~ for book_name,details in book_trally.items():
        # ~ print(f"\n- {book_name}:'作者':{details['作者']} '库存':{details['库存']} '价格':{details['价格']}")
    # ~ book_back = input(f"\n是否还书： ")
    # ~ book_back = book_back == '是'
        
        
    # ~ if book_back:
        # ~ return_name = input(f"\n请输入归还图书书名： ")
        # ~ return_amount = input(f"\n请确认归还图书数量： ")
        # ~ print("\n你需要支付的图书费用如下：")
        # ~ total_price = int(return_amount) * int(book_trally[return_name]['价格'])
        # ~ print(f"\n{total_price}元")
    
# ~ 练习12
store = {
    '苹果': {'价格': 3.5, '库存': 10, '描述': '新鲜的红苹果'},
    '香蕉': {'价格': 2.2, '库存': 15, '描述': '天然香蕉，富含钾元素'},
    '橙子': {'价格': 4.0, '库存': 20, '描述': '甜美的橙子，富含维生素C'},
    '西瓜': {'价格': 12.0, '库存': 5, '描述': '清爽的西瓜，夏天必备'},
}
trally = {}
empty = 0
for fruits_name,fruits_attributes in store.items():
    print(f"\n{fruits_name}:{fruits_attributes}")
    
while True:
    customers_info = input(f"\n请选择需要的商品： ")
    if customers_info == '':
        empty += 1
        if empty > 3:
            print(f"\n未选择商品，系统已退出")
            break
    if customers_info == 'quit':
        break 
    if customers_info in store:
        buyed_amount = input(f"\n请输入需要购买的数量： ")
        
        try:
            buyed_amount = int(buyed_amount)
        except ValueError:
            print(f"\n请输入有效数字： ")
            continue
        if buyed_amount > store[customers_info]['库存']:
            print(f"\n库存不足，请重新购买： ")
            continue   
        else:
            store[customers_info]['库存'] -= buyed_amount
            # ~ 判断用户输入名字是否在购物车中，第一次肯定不在，那么就执行else,
            # ~ 将水果所有信息建立到购物车中，如果第二次购买同样的水果，
            # ~ 水果信息已经在购物车中，那么就执行if,叠加数量，
            # ~ 如果不是同样的水果，那么依然执行else,
            # ~ 如果没有这个判断，除了每次叠加水果数量只外，
            # ~ 其余信息都会覆盖之前的水果信息。
            if customers_info in trally:
                trally[customers_info]['数量'] += buyed_amount
            else:
                trally[customers_info]={'价格':store[customers_info]['价格'],'数量':buyed_amount,'描述':store[customers_info]['描述']}
        continu_info = input(f"\n你购买的商品已加入购物车，请问是否继续选购： ")
        if continu_info == '是':
            print(f"\n{trally}")
            continue
        else:
            break 
    else:
        print(f"\n商品不存在，请重新输入： ")
        continue        
if trally:
    
    print(f"\n你购买的商品如下： ")
    unit_price = 0 
    total_price = 0               
    for name,detail in trally.items():
        unit_price = float(detail['价格']) * float(detail['数量'])
        # ~ print(f"\n- {name}: 数量:{detail['数量']} 总价：{unit_price:.2f}")先把每个水果的价格打印出来，避免最后只输出最后的水果信息
        total_price += unit_price
print(f"\n总价:{total_price:.2f}元")    

            
            
            
            
       
        
        
        
        
        
        
        
        
        
   
        
    
        
              
        
            
                
                
                
                
                
                
                
                
                
      
        
            
 












        
        
        












