#-*- coding:utf-8 _*- 
""" 
@file: stringJoin.py 
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
#x=”abc”,y=”def”,z=[“d”,”e”,”f”],分别求出x.join(y)和x.join(z)返回的结果

x = 'abc'
y = 'def'
z = ['d', 'e', 'f']

#返回一个字符串，它是字符串中字符串的串联可迭代的。 元素之间的分隔符是S。

print(x.join(y))   #dabceabcf  以 x 做分隔符
print('*'.join(y)) #d*e*f  以 * 做分隔符
print(x.join(z))   #dabceabcf