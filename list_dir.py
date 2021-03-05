# -*- coding:utf-8 _*-
""" 
@file: list_dir.py 
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
使用代码实现查看列举目录下的所有文件
'''

import os


def dirpath(lpath, lfilelist: list):
    list_dir = os.listdir(lpath)
    for f in list_dir:
        file = os.path.join(lpath, f)  # 拼接完整路径
        if os.path.isdir(file):  # 判断如果为空文件夹则进行递归遍历
            dirpath(file, lfilelist)
        else:
            lfilelist.append(file)
    return lfilelist


lfilelist = dirpath(os.getcwd(), [])  # 获取当前文件所在的文件夹
for f in lfilelist:
    print(f)
