#-*- coding:utf-8 _*- 
""" 
@file: inner.py 
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

'''
如何理解闭包
https://www.cnblogs.com/zhuifeng-mayi/p/9218762.html

在一个外函数中定义了一个内函数，内函数里运用了外函数的临时变量，并且外函数的返回值是内函数的引用。这样就构成了一个闭包
'''

def outer(a):  #外部函数
    b = 10     #外函数的临时变量
    def inner(): #内部函数
        print(a+b) #内部函数调用了外函数的临时变量
    return inner   #返回内部函数


if __name__ == '__main__':
    demo = outer(5)
    demo()
    demo = outer(7)
    demo()
    print(demo.__delattr__())