# -*- coding:utf-8 _*-
""" 
@file: recursive.py 
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
递归算法理解
'''


# 计算阶乘
def factorial(n: int):
    if not n:
        return
    if int(n) <= 2:
        return n

    # factorial(n) = factorial(n-1) * n  等价关系式
    return factorial(n - 1) * n


# 斐波那契数列的是这样一个数列：1、1、2、3、5、8、13、21、34....，即第一项 f(1) = 1,第二项 f(2) = 1.....,第 n 项目为 f(n) = f(n-1) + f(n-2)。求第 n 项的值是多少。
def Fibonacci(n):
    if int(n) <= 2:
        return 1
    # 找出等价关系式
    return Fibonacci(n - 1) + Fibonacci(n - 2)


# 递归优化
arry = []

def f(n):
    if n <= 1:
        return n
    if arry[n] != -1:
        return arry[n]
    else:
        arry[n] = f(n - 1) + f(n - 2)
        return arry[n]


if __name__ == '__main__':

    n1 = factorial(10)
    n2 = Fibonacci(10)
    print(f"阶乘:{n1}")
    print(f"斐波那契数列:{n2}")
