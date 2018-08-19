'''
题目描述
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead or not pHead.next or not pHead.next.next:
            return None
        slow = pHead.next
        fast = pHead.next.next
        while slow != fast:
            #判断链表成不成环
            if not slow.next or not fast.next.next:
                return None
            slow = slow.next
            fast = fast.next.next
        #成环的话，出上一个循环慢指针刚好走完一个环的步数
        #快指针走了比慢指针多一个环的步数
        fast = pHead
        #快指针重置位置到链表头，这样两指针差一个环的距离了
        while slow != fast:
            #同样速度前进至再碰头，即是入口节点的位置了
            slow = slow.next
            fast = fast.next
        return fast

