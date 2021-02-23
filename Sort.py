# -*- coding:utf-8 _*-
""" 
@file: Sort.py
@time: 2021/02/23
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

'''
字符串去重并按顺序返回
'''
s = 'ajldjlajfdljfdddjhujajddjadjnajkdaoncgbcyuhvbqq1451451'
l = list(set(s))
l.sort(reverse=False)  # sort()方法无返回值
print(''.join(l))

# 字典根据键从小到大排序  dict={“name”:”zs”,”age”:18,”city”:”深圳”,”tel”:”1362626627”}

dic = {"name": "zs", 'age': 18, 'city': "深圳", 'tel': "1362626627"}

print(dic.items())

# 以键值对中 key 的首字母排序
l = sorted(dic.items(), key=lambda i: i[0], reverse=False)
print(l)

# 利用collections库的Counter方法统计字符串每个单词出现的次数”kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h”
from collections import Counter

a = 'kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h'

res = Counter(a)
print(res)

# 求出列表所有奇数并构造新列表，a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = list(map(lambda x: x % 2 == 1, a))
print(b)

#利用filter函数
def is_odd(n):
    return n%2 == 1
print(list(filter(is_odd, [1,2,3,4,5,6,7,8,9])))