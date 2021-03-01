# -*- coding:utf-8 _*-
""" 
@file: Fibonacci.py 
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

'''
0 1 1 2 3 5 8 13 21 34 55
斐波那契数列----yield 用法
'''


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(f"b的值：{b}")
        yield b  # 使用 yield ，相当于return,下一步直接从这里开始执行
        # print(f"a:{a},b:{b}")
        a, b = b, a + b
        print(f"a>>>{a},b>>>{b}")
        n += 1


# 递归写法
# 斐波那契数列的是这样一个数列：0、1、1、2、3、5、8、13、21、34....，即第一项 f(1) = 1,第二项 f(2) = 1.....,第 n 项目为 f(n) = f(n-1) + f(n-2)。求第 n 项的值是多少。
def Fibonacci(n):
    if int(n) <= 2:
        return 1
    # 找出等价关系式
    return Fibonacci(n - 1) + Fibonacci(n - 2)


f = fab(11)
for i in range(10):
    print(next(f))
