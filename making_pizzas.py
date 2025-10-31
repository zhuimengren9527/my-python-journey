# ~ 函数模块调用

# ~ 方法一

# ~ import module

# ~ module.make_pizza(16,'pepperoni')
# ~ module.make_pizza(12,'mushrooms','green penpers','extra cheese')

# ~ 方法二

# ~ from module import make_pizza

# ~ make_pizza(16,'pepperoni')
# ~ make_pizza(12,'mushrooms','green penpers','extra cheese')


# ~ 方法三（指定别名，避免函数名与主程序变量名重复）

# ~ from module  import make_pizza as mp

# ~ mp(16,'pepperoni')
# ~ mp(12,'mushrooms','green penpers','extra cheese')



# ~ 方法四

# ~ import module as p

# ~ p.make_pizza(16,'pepperoni')
# ~ p.make_pizza(12,'mushrooms','green penpers','extra cheese')



# ~ 方法5

from module import *

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green penpers','extra cheese') 
