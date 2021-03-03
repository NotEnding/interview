# -*- coding:utf-8 _*-
""" 
@file: binary_search.py 
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

'''
二分查找
1.列表必须是顺序存储结构
2.必须按关键字大小有序排列
'''


def binary_search(data_list, val):
    """
    :param data_list: 有序列表
    :param val: 要获取索引的值
    :return:
    """
    min = 0  #最小索引
    max = len(data_list) - 1  #最大索引
    while min <= max:
        mid = (min + max) // 2     #中间数下标
        if data_list[mid] == val:  #如果中间数正好等于val
            return mid
        elif data_list[mid] > val: #如果val小于中间数，在中间数左边，则max确定为mid-1
            max = mid - 1
        else:                      #如果val大于中间数，在中间数右边，则min确定为mid+1
            min = mid + 1
    return  #val不存在，则返回None


if __name__ == '__main__':
    data_list = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    val = int(input(f"请输入要查找的元素值："))
    index = binary_search(data_list,val)
    if not index:
        print(f"元素不在数组中")
    else:
        print(f"您要查找的元素在列表中的索引位置：{index}")