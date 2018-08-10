'''
题目描述
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
'''

# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        tmp = 1
        n = len(A)
        #把每个待求数分成两部分写
        #注意边界
        #不行画图
        a1 = [1]
        a2 = [1]
        ans = []
        for i in range(n-1):
            a1.append(a1[-1]*A[i])
        for i in range(1,n):
            a2.append(a2[-1]*A[-i])
        a2 = a2[::-1]
        for i in range(n):
            ans.append(a1[i]*a2[i])
        return ans