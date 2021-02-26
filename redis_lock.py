# -*- coding:utf-8 _*-
""" 
@file: redis_lock.py 
@time: 2021/02/26
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
redis 分布式锁 --python实现
'''
# 连接redis
import time
import uuid
import hashlib
from threading import Thread

import redis

redis_client = redis.Redis(host="localhost",
                           port=6379,
                           password='1234qwer',
                           db=1)


# 获取一个锁
def acquire_lock(lock_name, acquire_time=10, time_out=10):
    """
    :param lock_name: 锁名称
    :param acquire_time: 客户端等待获取锁的时间
    :param time_out: 锁的超时时间
    :return:
    """
    """获取一个分布式锁"""
    end = time.time() + acquire_time
    lock = "string:lock:" + lock_name
    # identifier = str(uuid.uuid4())
    identifier = hashlib.sha256(lock.encode()).hexdigest() #以锁名称生成一个hash字符串
    while time.time() < end:
        if redis_client.setnx(lock, identifier):
            # 给锁设置超时时间, 防止进程崩溃导致其他进程无法获取锁
            redis_client.expire(lock, time_out)
            return identifier
        elif not redis_client.ttl(lock):
            redis_client.expire(lock, time_out)
        time.sleep(0.001)
    return False


# 释放一个锁
def release_lock(lock_name, identifier):
    """通用的锁释放函数"""
    lock = "string:lock:" + lock_name
    pip = redis_client.pipeline(True)
    while True:
        try:
            pip.watch(lock)
            lock_value = redis_client.get(lock)
            if not lock_value:
                return True

            if lock_value.decode() == identifier:
                pip.multi()
                pip.delete(lock)
                pip.execute()
                return True
            pip.unwatch()
            break
        except redis.excetions.WacthcError:
            pass
    return False


'''
例子中使用50个线程模拟秒杀10张票，使用–运算符来实现商品减少，从结果有序性就可以看出是否为加锁状态。
'''

count = 10  # 总计10张票


def seckill(i):
    identifier = acquire_lock('resource')
    print("线程:{}--获得了锁".format(i))
    time.sleep(1)
    global count
    if count < 1:
        print("线程:{}--没抢到，票抢完了".format(i))
        return
    count -= 1
    print("线程:{}--抢到一张票，还剩{}张票".format(i, count))
    release_lock('resource', identifier)


for i in range(50):
    t = Thread(target=seckill, args=(i,))
    t.start()



'''
1、获取锁的时候，使用setnx加锁，并使用expire命令为锁添加一个超时时间，超过该时间则自动释放锁，锁的value值为一个随机生成的UUID，通过此在释放锁的时候进行判断。
2、获取锁的时候还设置一个获取的超时时间，若超过这个时间则放弃获取锁。
3、释放锁的时候，通过UUID判断是不是该锁，若是该锁，则执行delete进行锁释放
'''