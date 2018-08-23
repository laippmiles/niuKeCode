'''
题目描述

输入两个链表，找出它们的第一个公共结点。
'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getLen(self, pHead):
        p = pHead
        count = 0
        while p:
            count += 1
            p = p.next
        return count

    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        count1 = self.getLen(pHead1)
        count2 = self.getLen(pHead2)
        #先搞到两个链表的长度
        #长的先走几步
        #然后长短的一块走，走到的第一个相同的即为所求
        p1 = pHead1
        p2 = pHead2
        n = abs(count1 - count2)
        if count1 > count2:
            for i in range(n):
                p1 = p1.next
        elif count2 > count1:
            for i in range(n):
                p2 = p2.next
        while p1 and p2:
            if p1.val == p2.val:
                return p1
            p1 = p1.next
            p2 = p2.next
        return None
