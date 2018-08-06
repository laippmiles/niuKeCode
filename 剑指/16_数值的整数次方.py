'''
题目描述
给定一个double类型的浮点数base和int类型的整数exponent。
求base的exponent次方。
'''

# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0:
            return 0
        #考虑这个特殊情况
        return base ** exponent
        #这部用python的便利功能即可