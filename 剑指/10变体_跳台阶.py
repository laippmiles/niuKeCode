'''
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
'''

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        elif number == 2:
            return 2
        f2 = 2
        ans = 3
        if number == 3:
            return ans
        for i in range(4,number+1):
            tep = f2
            f2 = ans
            ans += tep
        return ans