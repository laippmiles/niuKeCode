'''
题目描述
定义栈的数据结构，
请在该类型中实现一个能够得到栈中所含最小元素的min函数
（时间复杂度应为O（1））。
'''

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minnum = []
        #重点在最小数辅助栈上
    def push(self, node):
        # write code here
        if len(self.stack)==0:
            self.stack.append(node)
            self.minnum.append(node)
            #用辅助栈记录当前数据最小值的情况
        else:
            self.stack.append(node)
            if node < self.minnum[-1]:
                self.minnum.append(node)
            else:
                self.minnum.append(self.minnum[-1])
    def pop(self):
        # write code here
        self.stack.pop()
        self.minnum.pop()
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.minnum[-1]