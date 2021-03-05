# -*- coding:utf-8 _*-
""" 
@file: dest-sum.py 
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
Given an array of integers, return indices of the two numbers such that they add up to a specific target.You may assume that each input would 
have exactly one solution, and you may not use the same element twice.
Example:
          Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
           return [0, 1]

中文描述：在一个列表中查找两个值得和等于目标值，并返回索引
问题是要从数组中找到两个数据，使得两数之和等于目标值，输出该两数的下标（从0开始）
'''


def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    i = 0
    j = -1
    while i <= (len(numbers)) and abs(j) <= (len(numbers)):
        if numbers[i] + numbers[j] < target: #从前往后
            i += 1
        elif numbers[i] + numbers[j] > target: #从后往前
            j -= 1
        else:
            return [i + 1, len(numbers) + j + 1]
    return []


if __name__ == '__main__':
    nums  = [1,4,5,8,9,10,15,23,56,182]
    index = twoSum(nums,25)
    print(index)