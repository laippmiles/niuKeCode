'''
题目描述

输入n个整数，找出其中最小的K个数。
例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
'''

# -*- coding:utf-8 -*-
class Solution:
    #次优解
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput):
            return []
        tinput.sort()
        #python自带的sort复杂度是O(nlogn)
        return tinput[:k]

# -*- coding:utf-8 -*-
class Solution1:
    #用python的堆函数
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        import heapq
        if k <= len(tinput):
            return heapq.nsmallest(k,tinput)
        else:
            return []