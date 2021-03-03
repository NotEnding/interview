# -*- coding:utf-8 _*-
""" 
@file: fast_search.py 
@time: 2021/03/03
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

"""
快速排序
"""


def fast_search(data_list):
    if len(data_list) < 2:
        return data_list
    else:
        pivot = data_list[0]
        small = [i for i in data_list[1:] if i <= pivot]
        big = [j for j in data_list[1:] if j > pivot]
        return fast_search(small) + [pivot] + fast_search(big)


if __name__ == '__main__':
    data_list = [6, 18, 23, 5, 7, 4, 13, 2, 1, 13, 5, 6]
    new_list = fast_search(data_list)
    print(new_list)
