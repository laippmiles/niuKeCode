'''
题目描述
输入一个链表，反转链表后，输出新链表的表头。
'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        ans = None
        p = pHead

        while p:
            temp = p.next
            p.next = ans
            ans = p
            p = temp
            #旧链表的头部依次接入新链表，出来即时翻转链表了
            #这个方法鲁棒过关，简单够用
        return ans