'''
题目描述
如何得到一个数据流中的中位数？
如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
'''

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.l = []
    def Insert(self, num):
        # write code here
        self.l.append(num)
        self.l.sort()
        #每次来新数据就排序。偷懒法
    def GetMedian(self,l):
        # write code here
        s = len(self.l)
        if s % 2 == 1:
            return self.l[int(s/2)]
        else:
            return (self.l[int(s/2)]+self.l[int(s/2)-1])/2.0
            #注意这里要用个/2.0，否则会被去掉小数部分