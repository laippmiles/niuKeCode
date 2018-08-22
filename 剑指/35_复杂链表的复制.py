'''
题目描述
输入一个复杂链表
（每个节点中有节点值，以及两个指针，
一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
'''


# -*- coding:utf-8 -*-
class RandomListNode:
     def __init__(self, x):
         self.label = x
         self.next = None
         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here

        if not pHead:
            return pHead
        p = RandomListNode(pHead.label)
        p.next = pHead.next
        p.random = pHead.random

        nextp = pHead.next
        p.next = self.Clone(nextp)
        #使用递归一直复制往下的节点即可
        #递归停止的条件是pHead is None，返回一个None
        return p