# -*- coding:utf-8 _*-
""" 
@file: verify_code.py 
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

# 参考博客
'''
https://blog.csdn.net/qq_44484910/article/details/107324854
'''

# 题目要求
'''
某产品的⽤用户注册邀请码为⼀一串串有小写字母和数字组成的字符串串，字符串长度为16。当⽤用户数据邀 请码的时候，系统需要对邀请码做有效性验证，假设验证规则如下：
1、从序列列号最后一位字符开始，逆向将奇数位(1、3、5等等)相加；
2、从序列列号最后一位数字开始，逆向将偶数位数字，先乘以2（如果乘积为两位数，则将其减去 9），再求和；
3、将奇数位总和加上偶数位总和，结果可以被10整除；
4、小写字母对应数值，可由下面键值对确定； [(a,1), (b,2), (c,3)…,(i,9), (j,1), (k, 2)…]，亦即，按字⺟母顺序，1-9循环。

输⼊：输⼊入16位字符串，表示邀请码
输出：输出“ok”或者“error”
'''


def verify_code(code):
    """
    :param code: 16位字符串
    :return:
    """
    # 验证长度和格式 isalnum() 方法检测字符串是否由字母和数字组成。
    if len(code) != 16 or not isinstance(code, str) or not code.isalnum():
        print("不符合邀请码规则")
        return

    # 建立对应关系，满足条件4
    dic = dict()
    num = 1
    for alpha in "abcdefghijklmnopqrstuvwxyz":
        if num > 9:
            num = 1
        dic[alpha] = num
        num += 1

    _temp_list = list(code)[::-1]  # 逆向列表

    odd = 0  # 奇数位之和
    even = 0  # 偶数为之和

    for index, v in enumerate(_temp_list):
        index += 1
        # 取模-返回除法的余数,
        if index % 2:  # 奇数位处理
            if v.isalpha():  # 如果是字母
                _num = dic[v]
            else:
                _num = int(v)
            odd += _num
        else:  # 偶数位处理
            if v.isalpha():  # 如果是字母
                _num = (dic[v]) * 2
            else:
                _num = int(v) * 2
            if _num > 9:
                even += (_num - 9)
            even += _num

    print(f"odd:{odd}")
    print(f"even:{even}")

    # 验证结果
    if (odd + even) % 10:
        print("error")
    else:
        print("ok")


if __name__ == '__main__':
    code = input(f"请输入您的邀请码：")
    verify_code(str(code))
