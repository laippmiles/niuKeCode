'''
题目描述
在一个排序的链表中，存在重复的结点，
请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
'''

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        ans = ListNode(pHead.val-1)
        ans.next = pHead
        #建立一个链表新表头
        p = ans
        q = ans.next
        #建立p，q两个指针
        while q:
            while q.next and q.next.val == q.val:
                q = q.next
            if p.next != q:
                #如果p.next != q，遇到重复节点了，p接上q的下一个节点
                q = q.next
                p.next = q
            else:
                p = p.next
                q = q.next
                #无事发生的时候，p，q都走下一个节点
        return ans.next