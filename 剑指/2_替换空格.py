'''
题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''

# -*- coding:utf-8 -*-
#Python的看家本领算是
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        ans = ''
        for i in s:
            if i == ' ':
                ans += '%20'
            else:
                ans += i
        return ans