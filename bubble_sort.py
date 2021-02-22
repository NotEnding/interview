#-*- coding:utf-8 _*- 
""" 
@file: bubble_sort.py 
@time: 2021/02/20
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
https://blog.csdn.net/weixin_43790276/article/details/104033622
代码中，i 表示第几轮“冒泡”，j 表示“走访”到的元素索引。每一轮“冒泡”中，j 需要从列表开头“走访”到 len(array) - i 的位置。
时间复杂度   O(n^2)
'''


#增序排列
def bubble_sort_asc(array):
    for i in range(1, len(array)): #表示第几轮
        # print(f"当前第:{i}轮")
        for j in range(0, len(array) - i): #从列表开头走访到 len(array) - i
            # print(f"当前比较的元素索引:{j}")
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


#降序排列
def bubble_sort_desc(array):
    for i in range(1, len(array)):
        # print(f"当前第:{i}轮")
        for j in range(0, len(array) - i):
            # print(f"当前比较的元素索引:{j}")
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


if __name__ == '__main__':
    array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
    print(f"列表长度：{len(array)}")
    print(f"从小至大排列：",bubble_sort_asc(array))
    print(f"从大至小排列：",bubble_sort_desc(array))