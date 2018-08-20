'''
题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''

# -*- coding:utf-8 -*-
#分开考虑
#第一个块竖着放，接下来的步骤有f(n-1)种可能性
#第一个块横着放，那肯定有个块也要横着放，接下来的步骤有f(n-2)种可能性
#f(0) = 0,f(1) = 1,f(2) = 2,
#其实这个是斐波那契数列题的变体
class Solution:
    def rectCover(self, number):
        # write code here
        if number <= 2:
            return number
        f1 = 1
        ans = 2
        for i in range(3,number+1):
            tep = ans
            ans += f1
            f1 = tep
        return ans