# -*- coding: UTF-8 -*-
'''
@Author  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@WeChat     ：CoderWanFeng
@Blog      ：www.python-office.com
@Date    ：2023/6/24 0:22 
@Description     ：
'''

import pohan
from pohan.pinyin.pinyin import Style

pinyin_list = pohan.pinyin.han2pinyin("程序员晚枫", style=Style.TONE3)
print(pinyin_list)
