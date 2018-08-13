'''
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 1:
            return 1
        return 2 ** (number-2) *2
    #找规律问题2333
    #能意识到f(n) = f(n-1) + f(n-2) + ... + f(1)
    #f(2) = f(1) +1, f(1) = 1 基本就能做出来了