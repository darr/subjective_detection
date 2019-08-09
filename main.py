#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : main.py
# Create date : 2019-08-08 23:34
# Modified date : 2019-08-08 23:39
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from zhuguan import ZhuguanDetect

def run():
    handler = ZhuguanDetect()
    sent = '''中华人民共和国万岁'''
    score = handler.detect(sent)
    print(sent)
    print(score)

    sent = '''我喜欢你'''
    score = handler.detect(sent)
    print(sent)
    print(score)

if __name__ == '__main__':
    run()
