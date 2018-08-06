'''
题目描述
输入一个链表，输出该链表中倒数第k个结点。
'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#这道题极考鲁棒性，留意
class Solution:
    def FindKthToTail(self, head, k):
        # write code here\
        if k<=0 or head == None:
            return None
        p = head
        q = head
        for i in range(k-1):
            #这里用for更容易确定迭代次数，别作死用while了
            #以下判断放循环内
            if p.next is None:
                #注意这里的判定是p.next。要不最后一次会迭代到None
                return None
            p = p.next
        while p.next:
            p = p.next
            q = q.next
        return q