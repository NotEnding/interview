#-*- coding:utf-8 _*- 
""" 
@file: yield_from.py 
@time: 2021/03/05
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


def generator1():
    item = range(10)
    for i in item:
        yield i

def generator2():
    yield 'a'
    yield 'b'
    yield 'c'
    yield from generator1() #yield from iterable本质上等于 for item in iterable: yield item的缩写版
    yield from [11,22,33,44]
    yield from (12,23,34)
    yield from range(3)

for i in generator2() :
    print(i)
