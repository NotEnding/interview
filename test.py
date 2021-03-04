# -*- coding:utf-8 _*-
""" 
@file: test.py 
@time: 2021/03/01
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


# def fun(l=None):
#     if l is None:
#         l = []
#     l.append(1)
#     return l
#
#
# fun()
# fun()
# x = fun()
# print(x)

import inspect


def num():
    return [lambda x:i*x for i in range(4)]


# num 函数 等价于 func()
def func():
    fun_lambda_list = []

    for i in range(4):
        def lambda_(x):
            return x * i

        fun_lambda_list.append(lambda_)

    return fun_lambda_list

for m in num():
    print(inspect.getsource(m))
    print(m(2))

print([m(2) for m in num()])  #[6,6,6,6]

# 一行打印 九九乘法表
print('\n'.join([' '.join(["%2s x%2s = %2s"%(j,i,i*j) for j in range(1,i+1)]) for i in range(1,10)]))