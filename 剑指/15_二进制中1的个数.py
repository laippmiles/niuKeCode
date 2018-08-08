'''
题目描述
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n == 2**31*-1:
            return 1
            #正数最小值是特殊情况，特殊处理
        if n >= 0:
            n = bin(n)
            return n.count('1')
            #正数常规处理
        else:
            #负数补码是第一位为1，其余位0,1倒置后加一
            #负数的话，先补0到31位
            n = '0' * (31-len(bin(n)[3:])) +bin(n)[3:]
            ans = ''
            for i in n:
                if i == '1':
                    ans += '0'
                elif i == '0':
                    ans += '1'
            #0,1倒置
            ans = bin(int(ans,2)+1)
            #补1
            return ans.count('1')+1
            #加上负号那个1
