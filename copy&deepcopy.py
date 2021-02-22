#-*- coding:utf-8 _*- 
""" 
@file: copy&deepcopy.py 
@time: 2021/02/22
@site:  
@software: PyCharm 

# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛ 
"""

import copy

a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象

b = a  # 赋值，传对象的引用。a 和 b 都指向同一个对象。
c = copy.copy(a)  # 对象拷贝，浅拷贝。 a 和 c 是一个独立的对象，但他们的子对象还是指向统一对象（是引用）。
d = copy.deepcopy(a)  # 对象拷贝，深拷贝。a 和 d 完全拷贝了父对象及其子对象，两者是完全独立的。

print(f"原值：{a},a对象：{id(a)},a[4]对象：{id(a[4])}")
print(f"赋值：{b},b对象：{id(b)},b[4]对象：{id(b[4])}")   #可以看到赋值，b和a完全一致
print(f"浅拷贝：{c},c对象：{id(c)},c[4]对象：{id(c[4])}") #可以看到浅拷贝，c对象发生变化，但c中的子对象 c[4] 还是和 a[4]一致，子对象还是统一的
print(f"深拷贝：{d},d对象：{id(d)},d[4]对象：{id(d[4])}") #可以看到深拷贝，d对象发生变化，且d中的子对象也发生变化，完全独立

a.append(5)  # 修改对象a
a[4].append('c')  # 修改a中的子对象 ['a', 'b']

print('修改后：a = ', a)
print('修改后：b = ', b)  #b和a完全一致，所以全部发生变化
print('修改后：c = ', c)  #c中的子对象地址和a一致，所以c[4]会和a[4]一致，但c整体是一个独立的对象，所以不会有append(5)操作
print('修改后：d = ', d)  #d和a完全独立，所以什么都不会发生变化