#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/16 22:47
# @Author  : Paulson
# @File    : query.py.py
# @Software: PyCharm
# @define  : function
import json

import requests
from json import JSONDecodeError

FILENAME = 'city_code.txt'


def read_code(filename = FILENAME):
    with open(filename,'r') as f:
        city_code = json.load(f)
        print(city_code)
    return city_code

def query_code(table,city):
    '''
    :param table: 字典
    :param city:  字符串
    :return:
    '''
    try:
        code = table[city]
    except KeyError:
        raise
    return code

def query_weather(code):
    url = f'http://wthrcdn.etouch.cn/weather_mini?citykey={code}'
    print(url)

    try:
        response = requests.get(url)
    except requests.ConnectionError:
        raise

    try:
        info_json = response.json()
        print(info_json)
    except JSONDecodeError:
        return '无法查询'


    data = info_json['data']
    city = f"城市： {data['city']}\n"
    today = data['forecast'][0]
    print(today)
    date = f"日期： {today['date']}\n"
    now = f"实时温度：{data['wendu']}度\n"
    temperature = f"温度：{today['high']} {today['low']}\n"
    fengxiang = f"风向：{today['fengxiang']}\n"
    type = f"天气： {today['type']}\n"
    tips = f"贴士： {data['ganmao']}\n"

    return city + date + now + temperature + fengxiang + type + tips



