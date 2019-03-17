#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/16 22:26
# @Author  : Paulson
# @File    : city_data.py
# @Software: PyCharm
# @define  : function
import json
import re

import pandas as pd


# print(file.head())

# 匹配 City_ID 中的数字
def covert(x):
    pat = re.compile('(\d+)')
    return pat.search(x).group()


# 建立城市与代码之间的映射关系
def city2id(file):
    code_dict = {}
    key = "City_CN"
    value = "City_ID_map"

    for k,v in zip(file[key],file[value]):
        code_dict[k] = v
    return  code_dict


# 将所得的字典数据存储为 txt 文件
def save_txt(code_dict):
    with open('city_code.txt','w') as f:
        f.write(json.dumps(code_dict))


if __name__ == '__main__':
    file = pd.read_csv('china-city-list.csv')
    file = file.loc[:, ['City_ID', 'City_CN']]
    file['City_ID_map'] = file['City_ID'].map(covert)
    code_dict = city2id(file)
    save_txt(code_dict)
    # print(code_dict)
