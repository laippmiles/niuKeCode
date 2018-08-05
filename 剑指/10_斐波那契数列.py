'''
题目描述

大家都知道斐波那契数列，现在要求输入一个整数n，
请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
'''

# -*- coding:utf-8 -*-
#时间复杂度为O(n)
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        f1 = 1
        f2 = 1
        for i in range(3,n+1):
            tep = f2
            #备份f2
            f2 += f1
            f1 = tep
        return f2