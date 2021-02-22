#-*- coding:utf-8 _*- 
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
斐波那契数列----yield 用法
'''


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 使用 yield ，相当于return,下一步直接从这里开始执行
        print(f"a:{a},b:{b}")
        a, b = b, a + b
        print(f"a>>>{a},b>>>{b}")
        n = n + 1


f = fab(5)
for i in range(10):
    print(next(f))