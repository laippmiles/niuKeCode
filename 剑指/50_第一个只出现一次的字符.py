'''
题目描述
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置,
 如果没有则返回 -1（需要区分大小写）.
'''

# -*- coding:utf-8 -*-
#用字典构造哈希表
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        dicn = {}
        n = len(s)
        if len(s) == 0:
            return -1
        for i in range(n):
            if s[i] not in dicn:
                dicn[s[i]] = [1,i]
            else:
                dicn[s[i]][0] += 1
        dicn = sorted(dicn.items(),key = lambda x:(x[1][0],x[1][1]))
        #注意多条件排序的格式，最后是lambda x:(x[1][0],x[1][1])
        #dicn.items()出来的单个元素示例：（'a',(1,index)），搞清楚自己弄了啥结构
        if dicn[0][1][0] == 1:
            return dicn[0][1][1]
        else:
            return -1