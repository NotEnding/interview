# -*- coding:utf-8 _*-
""" 
@file: python_reflection.py 
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
python的反射，它的核心本质其实就是利用字符串的形式去对象（模块）中操作（查找/获取/删除/添加）成员，一种基于字符串的事件驱动！
'''

import python_reflection2


# 通过比较字符串
# def run():
#     inp = input("请输入您想访问页面的url： ").strip()
#     if inp == "login":
#         python_reflection2.login()
#     elif inp == "logout":
#         python_reflection2.logout()
#     elif inp == "home":
#         python_reflection2.home()
#     else:
#         print("404")


# 根据函数名进行映射
def run():
    inp = input("请输入您想访问页面的url： ").strip()
    if hasattr(python_reflection2, inp):  # 判断是否有这个成员
        func = getattr(python_reflection2, inp)
        func()
    else:
        print('404 not found')


if __name__ == '__main__':
    run()
