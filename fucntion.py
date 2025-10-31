# ~ def greet_user(username):
    # ~ print(f"Hello,{username.title()}!")
# ~ greet_user('renyadong')

# ~ def display_message(motto):
    # ~ print(f"\n{motto}")
# ~ display_message('我要开始学习函数了！祝我成功！')

# ~ def favorite_book(title):
    # ~ print(f"\nOne of my favorite books is {title}!")
# ~ favorite_book('Alice in Wonderland')

# ~ def describe_pet(animal_type,pet_name):
    # ~ print(f"\nI have a {animal_type}.")
    # ~ print(f"\nMy {animal_type}'s name is {pet_name}")
# ~ describe_pet('hamster','harry')
# ~ describe_pet('dog','willie')
# ~ describe_pet(animal_type='hamster',pet_name='harry')

# ~ def describe_pet(pet_name,animal_type='dog'):
    # ~ print(f"\nI have a {animal_type}.")
    # ~ print(f"\nMy {animal_type}'s name is {pet_name}")
# ~ describe_pet(pet_name='willie')

# ~ 练习1
# ~ def make_shirt(shirt_size,shirt_design):
    # ~ print(f"\n这件T恤的的尺码是{shirt_size},图样是{shirt_design}")
# ~ make_shirt(shirt_size='170cm',shirt_design='祥云')

# ~ def make_shirt(shirt_size,shirt_design='I love Python'):
    # ~ print(f"\n这件T恤的的尺码是{shirt_size},图样是{shirt_design}")
# ~ make_shirt(shirt_size='大号')
# ~ make_shirt(shirt_size='中号')
# ~ make_shirt(shirt_size='大号',shirt_design='我爱Python')

# ~ def describe_city(city_name,country_attribution='China'):
    # ~ print(f"\n{city_name} is in {country_attribution}")
# ~ describe_city(city_name='chengdu')
# ~ describe_city(city_name='New York',country_attribution='America')

# ~ def get_formatted_name(first_name,last_name):
    # ~ full_name = f"{first_name} {last_name}"
    # ~ return full_name.title()
# ~ musician = get_formatted_name('jimi','hendrix')
# ~ print(musician)

# ~ def get_formatted_name(first_name,middle_name,last_name):
    # ~ full_name = f"{first_name} {middle_name} {last_name}"
    # ~ return full_name.title()
    
# ~ musician = get_formatted_name('john','lee','hoooker')
# ~ print(musician)

# ~ def get_formatted_name(first_name,last_name,middle_name=''):
    # ~ if middle_name:
        # ~ full_name = f"{first_name} {middle_name} {last_name}"
    # ~ else:
        # ~ full_name = f"{first_name} {last_name}"
    # ~ return full_name
# ~ musician = get_formatted_name('john','hoooker')
# ~ print(musician)
    
# ~ musician = get_formatted_name('john','hoooker','lee')
# ~ print(musician)    
    
# ~ def build_person(first_name,last_name,age=None):
    # ~ person = {'first': first_name, 'last': last_name}
    # ~ if age:
        # ~ person['age'] = age 
        
    # ~ return person
    
# ~ musician = build_person('jimi','hendrix',age=27)
# ~ print(musician)
    
    
# ~ def get_formatted_name(first_name,last_name):
    
    # ~ full_name = f"{first_name} {last_name}"
    # ~ return full_name.title()
    
# ~ while True:
    # ~ print(f"\nPlease tell me your name: ")
    # ~ print("(enter 'q' at any time to quit)")
    # ~ f_name = input("First name： ")
    # ~ if f_name == 'q':
        # ~ break 
    # ~ l_name = input("Last name: ")
    # ~ if l_name == 'q':
        # ~ break 
    
    # ~ formatted_name = get_formatted_name(f_name,l_name)
    # ~ print(f"\nHello ,{formatted_name}!")    
    
    
    
    
    
# ~ def city_country(city_name,country_name):
    
    # ~ full_name = f"\n{city_name} {country_name}"
    # ~ return full_name.title()

# ~ info = city_country('santiago','chile')
# ~ print(info)
        
# ~ def make_album(artist_name,album_name):
    
    # ~ info = {'artist' :artist_name,'album':album_name}
    # ~ return info

# ~ while True:
    # ~ print("(enter 'q' at any time to quit)")
    # ~ art_name = input(f"\n请输入歌手名： ")
    # ~ if art_name == 'q':
        # ~ break
    
    # ~ alb_name = input(f"\n请输入专辑名： ")
    # ~ if alb_name == 'q':
        # ~ break
    
    # ~ name =  make_album(art_name,alb_name)
    # ~ print(f"\n{name}")
    
# ~ def make_book(author_name,book_title):
    
    # ~ dictionary = {'author':author_name,'book':book_title}
    # ~ return dictionary

# ~ while True:
    # ~ print("(enter 'q' at any time to quit)")
    # ~ a_name = input(f"\n请输入作者名字： ")
    # ~ if a_name == 'q':
        # ~ break
    # ~ b_name = input(f"\n请输入书名： ")
    # ~ if b_name == 'q':
        # ~ break 
    # ~ info = make_book(a_name,b_name)
    # ~ print(f"\n{info}")
    
# ~ def greet_users(names):
    # ~ for name in names:
        # ~ msg =f"Hello,{name.title()}!"
        # ~ print(msg)
        
# ~ usernames =['hannah','ty','margot']
# ~ greet_users(usernames)
    
    
# ~ def print_models(unprinted_designs,completed_models):
    # ~ while unprinted_designs:
        # ~ current_design = unprinted_designs.pop()
        # ~ print(f"\n{current_design}")
        # ~ completed_models.append(current_design)
# ~ def show_completed_models(completed_models):
    # ~ print(f"\nThe following models have been printed:")
    # ~ for completed_model in completed_models:
        # ~ print(f"\n{completed_model}")
# ~ unprinted_designs =['phone case','robot pendant','dodecahedron']
# ~ completed_models=[]
# ~ print_models(unprinted_designs,completed_models)
# ~ show_completed_models(completed_models)

# ~ def trasfer_function(old_table,new_table):
    # ~ while old_table:
        # ~ new_table.append(old_table.pop())
    
# ~ def show_function(showed_table):
    # ~ for content,serial in enumerate(showed_table,1):
        # ~ print(f"\n{serial}、{content}")
    
# ~ original_table = ['listening','speaking','reading','writing']    
# ~ rev_table = []    
# ~ copy_original_table = original_table[:]     
# ~ trasfer_function(copy_original_table,rev_table)    
    
# ~ show_function(rev_table)    
# ~ print(copy_original_table)    
    
# ~ def collect_information(*kwargs):
    # ~ print(f"\{kwargs}")
    
    
# ~ def collect_information(first_name,last_name,**kwargs):
    # ~ print(f"\nfirst name is:{first_name} ")
    # ~ print(f"\nlast name is :{last_name} ")
    # ~ print(f"\nadditional informations are :")
    # ~ for key,value in kwargs.items():
        # ~ print(f"\n{key}:{value}")
    # ~ return kwargs
# ~ user_info=['Yadong', 'Ren', {'height': 170, 'sex': 'man'}]

# ~ collect_information(user_info[0],user_info[1],**user_info[2])    

# ~ 练习1
# ~ orders = [
    # ~ ('张三', {'麻辣烫': 2, '泡椒凤爪': 1, '小龙虾': 3}),
    # ~ ('李四', {'牛肉拉面': 1, '宫保鸡丁': 2}),
    # ~ ('王五', {'火锅': 1, '蒸饺': 4}),
# ~ ]

# ~ def  order_info(customer_name,**menu):
    # ~ order_dic = {'姓名':customer_name,'菜单':menu}
    # ~ return  order_dic
    
# ~ def show_orders(show_order):
    # ~ for dic in show_order:
        # ~ print(f"\n{dic['姓名']}：")
        # ~ for dish_name,quality in dic['菜单'].items():
            # ~ print(f"\n{dish_name}:{quality}")
            
            
# ~ collect_order_info = []

# ~ for name, menu_info in orders:
    # ~ collect_order_info.append(order_info(name,**menu_info))


# ~ show_orders(collect_order_info)

# ~ 练习2

# ~ borrow_records = [
    # ~ ('Alice', {'活着': 7, '三体': 14}),
    # ~ ('Bob', {'平凡的世界': 10}),
    # ~ ('Charlie', {'红楼梦': 30, '水浒传': 20}),
# ~ ]

# ~ def  borrow_books_info(reader_name,**borrowing_info):
    # ~ dic_book_info = {'读者姓名':reader_name,'借阅信息':borrowing_info}
    # ~ return dic_book_info

# ~ def show_borrowing_info(show_info):
    # ~ for dic in show_info:
        # ~ print(f"\n{dic['读者姓名']}: ")
        # ~ for book_name,borrowing_time in dic['借阅信息'].items():
            # ~ print(f"{book_name}:{borrowing_time}")
            
# ~ collect_borrowing_info = []

# ~ for name,dic_info in borrow_records:
    # ~ collect_borrowing_info.append(borrow_books_info(name,**dic_info))

# ~ show_borrowing_info(collect_borrowing_info)

# ~ 练习3
student_scores = [
    ('Alice', {'数学': 90, '英语': 85, '科学': 88}),
    ('Bob', {'数学': 78, '英语': 92, '科学': 84}),
    ('Charlie', {'数学': 95, '英语': 89, '科学': 91}),
]

def scores_info(student_name,**discipline_score):
    dic_students_scores = {'姓名':student_name,'学科成绩':discipline_score}
    return dic_students_scores

def show_students_scores(show_scores):
    for dic in show_scores:
        print(f"\n{dic['姓名']}:")
        for discipline,score in dic['学科成绩'].items():
            print(f"{discipline}:{score}")
collect_students_scores = []
for name,scores in student_scores:
    collect_students_scores.append(scores_info(name,**scores))

show_students_scores(collect_students_scores)

















    
    
    
    
    
    
    
