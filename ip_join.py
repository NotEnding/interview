#-*- coding:utf-8 _*- 
""" 
@file: ip_join.py 
@time: 2021/03/04
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
请编写一个函数实现将IP地址转换成一个整数。如 10.3.9.12 转换规则为：

```
 10           00001010
 3            00000011
 9            00001001
 12           00001100
```

再将以上二进制拼接起来计算十进制结果：00001010 00000011 00001001 00001100 = ？
'''


def ipfunc(ip):
    a = ip.split('.')
    l = []
    for i in a:
        i = bin(int(i))[2:] #转成2进制，去掉前面的 0b
        i = i.rjust(8,'0') #不足8位的，在靠右对齐后，在前方填充
        l.append(i)
    s = ''.join(l)
    return s

s = ipfunc('10.3.9.12')
print(s)  # 00001010000000110000100100001100

# 二进制转10进制
print(int(s,2))  #167971084