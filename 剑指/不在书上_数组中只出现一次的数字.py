'''
题目描述

一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。
请写程序找出这两个只出现一次的数字。
'''

# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        dicn = {}
        #哈希表法
        for i in array:
            if i not in dicn:
                dicn[i] = 1
            else:
                dicn[i] += 1
        ans = []
        for k in dicn.keys():
            if dicn[k] == 1:
                ans.append(k)
        return ans