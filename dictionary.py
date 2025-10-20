# ~ alien_0 = {'color': 'green', 'points': 5}

# ~ print(alien_0['color'])
# ~ print(alien_0['points'])

# ~ alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# ~ print(f"The original position: {alien_0['x_position']}")

# ~ if alien_0['speed'] == 'slow':
    # ~ x_increment = 1
# ~ elif alien_0['speed'] == 'medium':
    # ~ x_increment = 2
# ~ else :
    # ~ x_increment = 3
# ~ alien_0['x_position'] = alien_0['x_position'] + x_increment
# ~ print(f"New position: {alien_0['x_position']}")

# ~ alien_0 = {'color': 'green', 'points': 5}
# ~ print(alien_0)

# ~ del alien_0['points']
# ~ print(alien_0)

# ~ favorite_languages = {
    # ~ 'jen': 'python',
    # ~ 'sarah': 'c',
    # ~ 'edward': 'rust',
    # ~ 'phil': 'python',
    # ~ }

# ~ language=favorite_languages['sarah'].title()
# ~ print(f"Sarah's favorite language is {language}.")

#   使用get()访问值
# ~ alien_0 = {'color': 'green', 'speed': 'slow'}
# ~ print(alien_0.get('points')) 

# ~ 练习
# ~ personal_massage = {
    # ~ 'first_name': 'yadong',
    # ~ 'last_name': 'Ren',
    # ~ 'age': 34 ,
    # ~ 'city': 'chengdu',
    # ~ }
# ~ print (personal_massage)
# ~ print(personal_massage['first_name'])
# ~ print (personal_massage.get('heigh'))   # 用get()打印不存在的值

# 遍历字典

# item
# ~ user_0 = {
    # ~ 'username': 'efermi',
    # ~ 'first': 'enrico',
    # ~ 'last': 'fermi',
    # ~ }
# ~ for key,value in user_0.item():
    # ~ print(f"\nkey: {key}")
    # ~ print(f"value:{value}")

# ~ # keys
# ~ favorite_languages = {
    # ~ 'jen': 'python',
    # ~ 'sarah': 'c',
    # ~ 'edward': 'rust',
    # ~ 'phil': 'python',
    # ~ }
    
# ~ friends = ['phil','sarah']
# ~ for name in favorite_languages.keys():
    # ~ print(f"Hi {name.title()}.")
    
    # ~ if name in friends:
        # ~ language = favorite_languages[name].title()
        # ~ print(f"\n\t{name.title()},I see you love {language.title()}.")

# ~ # values
# ~ favorite_languages = {
    # ~ 'jen': 'python',
    # ~ 'sarah': 'c',
    # ~ 'edward': 'rust',
    # ~ 'phil': 'python',
    # ~ }

# ~ print("The following languages have been mentionde:")
# ~ for language in set(favorite_languages.values()): # set()剔除重复项
    # ~ print(language.title())

# 练习
# ~ term = {'variable': '变量',
        # ~ 'loop': '循环',
        # ~ 'dictionary': '字典',
        # ~ 'iteration': '迭代',
        # ~ 'function': '函数',
        # ~ }
# ~ print(f"variable:{term['variable']}")
# ~ print(f"variable:\n\t{term['variable']}")
# ~ print(f"loop:\n\t{term['loop']}")
# ~ for key,value in term.items():
    # ~ print(f"{key}:{term[key]}")
    # ~ print(f"{key}\n\t{value}")
    
#   嵌套
# ~ alien_0 = {'color': 'green', 'points': 5}
# ~ alien_1 = {'color': 'yellow', 'points': 10}
# ~ alien_2 = {'color': 'red', 'points': 15}

# ~ aliens = [alien_0, alien_1, alien_2] #  将3个字典合成一个列表

# ~ for alien in aliens:
    # ~ print(alien)

# ~ aliens = []

# ~ for alien_number in range(30):
    # ~ new_alien = {'color': 'green', 'points': 5,'speed': 'slow'}
    # ~ aliens.append(new_alien)
    
# ~ for alien in aliens[:3]:
    # ~ if alien['color'] == 'green':
        # ~ alien['color'] = 'yellow'
        # ~ alien['points'] = 10
        # ~ alien['speed'] = 'medium'
    
    
# ~ for alien in aliens[:30]:
    # ~ print(alien)
    # ~ print(len(aliens))

# ~ pizza = { 
    # ~ 'crust': 'thick',
    # ~ 'toppings': ['mushrooms', 'extra cheese'],
    # ~ }

# ~ print(f"\nYou ordered a {pizza['crust']}-crust pizza"
    # ~ "with the following pizza:")
    
# ~ for topping in pizza['toppings']:
    # ~ print(f"\n\t{topping}")  
    
# ~ # 练习1
# ~ groups = {
    # ~ 'A组': ['小明', '小红', '小刚'],
    # ~ 'B组': ['小丽', '小华', '小强'],
    # ~ 'C组': ['小王', '小李']
# ~ }

# ~ for group,students in groups.items():
    # ~ print(f"小组{group} 有以下学生：")


    # ~ for student in students:
        # ~ print(student)
    # ~ print()
    
# ~ #   练习2
# ~ bookshelves = {
    # ~ '第一排': ['Python入门', '数据结构', '算法基础'],
    # ~ '第二排': ['操作系统', '计算机网络'],
    # ~ '第三排': ['人工智能', '机器学习', '深度学习']
    # ~ }    
    
# ~ for row,books in bookshelves.items():
    # ~ print(f"{row}有以下这些书籍：")
    
    # ~ for book in books:
        # ~ print(f"- {book}")
    # ~ print()

# ~ #   练习3
# ~ bookshelves = {
    # ~ '第一排': ['Python入门', '数据结构', '算法基础'],
    # ~ '第二排': ['操作系统', '计算机网络'],
    # ~ '第三排': ['人工智能', '机器学习', '深度学习']
    # ~ }

# ~ for number in range(3):

    # ~ for row,books in bookshelves.items():
        # ~ print(f"书架{number}:{row} 有以下书籍:")
        
        # ~ for book in books:
            # ~ print(f"{number}.{book}")

#   综合练习1
# ~ library = {
    # ~ '第一排': [
        # ~ {'title': 'Python入门', 'available': True},
        # ~ {'title': '数据结构', 'available': False},
        # ~ {'title': '算法基础', 'available': True}
        # ~ ],
    # ~ '第二排': [
        # ~ {'title': '操作系统', 'available': True},
        # ~ {'title': '计算机网络', 'available': False}
        # ~ ]
    # ~ }

# ~ for row ,books in library.items():
    # ~ print(f"{row} 有以下书籍：")
    
    # ~ for book in books:
        # ~ print(f"- {book['title']}")
    
        # ~ if book['available']:
            # ~ print('状态:可借')
        # ~ else:
            # ~ print('状态:不可借')
    # ~ print()

# ~ #   综合练习2
# ~ students_scores = {"Alice": {"math": 88, "english": 92, "science": 79},
    # ~ "Bob": {"math": 75, "english": 85, "science": 90},
    # ~ "Charlie": {"math": 95, "english": 80, "science": 87}
    # ~ }

# ~ for name,subjects in students_scores.items():
    # ~ print(f"{name}的成绩是：")
    
    # ~ total = sum(subjects.values())
    # ~ number = len(subjects)
    # ~ avg = total / number
    
    # ~ for subject,score in subjects.items():
    
        # ~ if avg >= 90:
            # ~ level = '优秀'
        # ~ elif avg >= 75:
            # ~ level = '良好'
        # ~ else:
            # ~ level = '一般'
        # ~ print(f"平均分：{avg:.1f},综合评价：{level}")
    # ~ print()
    
# ~ #   综合练习3
# ~ library_seats = {
    # ~ '第一排': [
        # ~ {'occupied': False, 'power': True},
        # ~ {'occupied': True,  'power': False},
        # ~ {'occupied': False, 'power': False},
    # ~ ],
    # ~ '第二排': [
        # ~ {'occupied': True,  'power': True},
        # ~ {'occupied': False, 'power': False},
    # ~ ]
# ~ }

# ~ for rows,seats in library_seats.items():
    # ~ print(f"{rows}座位情况：")
   
    # ~ number = 0
    # ~ for seat in seats:
        # ~ if seat['occupied'] == True:
            # ~ status = "已占用"
        # ~ else:
            # ~ status = "空闲"
        
        # ~ if seat['power'] == True:
            # ~ socket = "有插座"
        # ~ else:
            # ~ socket ="无插座"
        # ~ number += 1
        
        # ~ print(f"- 座位{number}: {status},{socket}")
    # ~ print()
    
#   综合练习4
cinema_seats = {
    '第一排': [
        {'occupied': False, 'VIP': True},
        {'occupied': True, 'VIP': False},
        {'occupied': False, 'VIP': False},
    ],
    '第二排': [
        {'occupied': True, 'VIP': True},
        {'occupied': False, 'VIP': False},
    ]
}
for rows,seats in cinema_seats.items():
    print(f"{rows}座位情况：")
    number = 0
    for seat in seats:
        if seat['occupied'] == True:
            status = "已占用"
        else:
            status = "空闲"
            
        if seat['VIP'] == True:
            vips = "VIP"
        else:
            vips = "非VIP"
        
        number += 1
        
        print(f"- 座位{number}:{status},{vips}")
    print()



























