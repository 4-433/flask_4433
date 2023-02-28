# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/14 9:54
@Auth ： 冯珂
@File ：communal.py
@IDE ：PyCharm
@Motto: 
"""
from datetime import datetime
from decimal import Decimal


def get_int_now():
    """
    生成日期连续字符串
    :return:
    """
    dt = datetime.now()
    month = str(dt.month) if dt.month > 9 else '0' + str(dt.month)
    day = str(dt.day) if dt.day > 9 else '0' + str(dt.day)
    hour = str(dt.hour) if dt.hour > 9 else '0' + str(dt.hour)
    minute = str(dt.minute) if dt.minute > 9 else '0' + str(dt.minute)
    second = str(dt.second) if dt.second > 9 else '0' + str(dt.second)
    return int(str(dt.year) + month + day + hour + minute + second)


def random_str(num):
    """
    生成一个指定长度的随机字符串
    """
    import random
    stochastic = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(num):
        stochastic += base_str[random.randint(0, length)]
    return stochastic


def random_int(num):
    """
    生成一个指定长度的随机整数
    """
    import random
    stochastic = ''
    base_str = '0123456789'
    length = len(base_str) - 1
    for i in range(num):
        stochastic += base_str[random.randint(0, length)]
    return stochastic
