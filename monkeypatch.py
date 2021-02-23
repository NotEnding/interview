#-*- coding:utf-8 _*- 
""" 
@file: monkeypatch.py 
@time: 2021/02/23
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


''''
猴子补丁
'''

import requests

#源代码
def get_page(url):
	try:
		s = requests.get(url)
	except requests.HTTPError as e:
		print("HTTPError")

def get(url):
	raise requests.HTTPError


'''
我们为requests.get打了猴子补丁，这样我们就可以测试get_page方法能否正确处理异常了，
这样做既不需要为requests.get构造能抛出异常的url 输入参数，也不需要改变requests.get的源代码。
'''

if __name__ == "__main__":
	requests.get = get    #猴子补丁
	get_page("123")