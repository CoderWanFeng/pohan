# -*- coding: UTF-8 -*-
'''
@Author  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@WeChat     ：CoderWanFeng
@Blog      ：www.python-office.com
@Date    ：2023/4/9 19:26 
@Description     ：
'''
import office
from search4file import search_by_content

"""
功能关键词
"""

################# Excel #################

创建Excel = office.excel.fake2excel
Excel转PDF = office.excel.excel2pdf

################# PDF #################
加密PDF = office.pdf.encrypt4pdf
PDF转图片 = office.pdf.pdf2imgs
PDF加水印 = office.pdf.add_watermark_by_parameters

################# 图片 #################

下载图片 = office.image.down4img
图片加水印 = office.image.add_watermark

################# Word #################

Word转PDF = office.image.docx2pdf
合并Word = office.image.merge4docx
doc转docx = office.image.doc2docx
docx转doc = office.image.docx2doc

################# 文件 #################

批量重命名 = office.file.replace4filename
通过内容查找 = search_by_content
拿到所有文件 = office.file.get_files

################# PPT #################

PPT批量转PDF = office.ppt.ppt2pdf

################# 微信机器人 #################

自动发信息 = office.wechat.send_message
自动发文件 = office.wechat.send_file
