bicycles=['trek','cannondale','redline','specialized']
print(bicycles)
#   访问列表元素
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[0].upper())
print(bicycles[-1].title())  #访问列表最后一个元素
message=f"My first bicycle was a {bicycles[0].title()}."    #创建一条消息
print(message)

#   原始列表
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

#   修改元素
motorcycles[0]='ducati'
print(motorcycles)

#   添加元素
motorcycles.append('ducati')
print(motorcycles)

#   创建空列表添加元素
motorcycles=[]
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles,"\n")

#   任意位置插入元素
motorcycles.insert(0,'ducati')
print(motorcycles,"\n")

#删除元素

#   根据索引删除 del
motorcycles=['honda','yamaha','suzuki']
del motorcycles[0]
print(motorcycles,"\n")

#   删除列表最后一个元素并赋值给另一个变量
motorcycles=['honda','yamaha','suzuki']
print(motorcycles,"\n")

popped_motorcycle=motorcycles.pop() #   将删除元素赋值给变量popped_motorcycle
print(motorcycles)  #   打印删除最后一个元素后的列表
print(popped_motorcycle,"\n")    #   打印被删除的元素

#   创建一条消息指明被删除的元素是
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
last_owned=motorcycles.pop()
print(f"The motorcycle I ownde was {last_owned.title()}.","\n")

#   使用pop删除任意位置元素
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
first_owned=motorcycles.pop(0)
print(motorcycles)
print(f"The first motorcycle I owned was {first_owned.title()}.","\n")

#   根据元素的值删除 remove
motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)

motorcycles.remove('suzuki')
print(motorcycles,"\n")

#   继续使用remove后的值
motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)

too_expensive='ducati'
motorcycles.remove(too_expensive)
print(f"\n A {too_expensive.title()} is too expensive for me!","\n")

#   练习
guest=['A','B','C','D','E']
guest_str=", ".join(guest[:-1]) + " and " + guest[-1]
print(f"I want to invite {guest_str} to share a supper with me!","\n")
print(f"D won't be able to keep the appointment!","\n")
guest[3]="F"
print(guest)
guest_str= ", ".join(guest[:-1]) + " and " + guest[-1]
print(f"I cordially invite {guest_str}  to share a supper with me!")
guest.insert(0,"G")
print(guest)
guest.insert(3,"H")
print(guest)
guest.append("k")
print(guest)
print(f"I cordially invite {', '.join(guest[:-1])}  and  {guest[-1]} to share a supper with me!")
print(f"Due to the delayed delivery of the newly purchased dining table, I have decided to invite only two guests to join me for supper.")
guest.pop()
print(guest)
print(f"I’m terribly sorry, but I’m unable to invite you to dinner.")
guest.pop()
print(guest)
print(f"I’m terribly sorry, but I’m unable to invite you to dinner.")
guest.pop()
print(guest)
print(f"I’m terribly sorry, but I’m unable to invite you to dinner.")
guest.pop()
print(guest)
print(f"I’m terribly sorry, but I’m unable to invite you to dinner.")
guest.pop()
print(guest)
print(f"I’m terribly sorry, but I’m unable to invite you to dinner.")
guest.pop()
print(guest)
print(f"I’m terribly sorry, but I’m unable to invite you to dinner.")
del guest[0]
print(guest)
del guest[0]
print(guest)
