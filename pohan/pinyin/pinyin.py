# -*- coding: UTF-8 -*-
'''
@Author  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@WeChat     ：CoderWanFeng
@Blog      ：www.python-office.com
@Date    ：2023/6/23 23:33 
@Description     ：
'''

from pypinyin import pinyin, Style

STYLE = Style
def han2pinyin(hans, style=STYLE.NORMAL, heteronym=False, errors='default', strict=True, v_to_u=False,
               neutral_tone_with_five=False):
    return pinyin(hans, style, heteronym, errors, strict, v_to_u,
                  neutral_tone_with_five)


if __name__ == '__main__':
    print(pinyin('中心', style=Style.NORMAL))
