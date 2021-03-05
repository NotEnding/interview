# -*- coding:utf-8 _*-
""" 
@file: three_num.py 
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
有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？

分析：四个数字组成三位数，把三位数分为个、十、百位，将1、2、3、4填入其中，去掉不满足条件的剩下就是结果。
'''


def three_num():
    count = 0  # 计数
    nums = []  # 初始化
    for i in range(1, 5):  # 百位
        for j in range(1, 5):  # 十位
            for k in range(1, 5):  # 个位
                if (i != j) and (i != k) and (j != k):  # 判断不重复的三个数
                    num = 100 * i + 10 * j + k
                    count += 1
                    if num not in nums:
                        nums.append(num)
    return count, nums


if __name__ == '__main__':
    count, nums = three_num()
    print(f"总共有{count}个,列表{nums},列表长度{len(nums)}")
