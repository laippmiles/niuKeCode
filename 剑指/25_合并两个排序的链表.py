'''
题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，
当然我们需要合成后的链表满足单调不减规则。
'''

# -*- coding:utf-8 -*-
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
class Solution:
    # 返回合并后列表
    #看图说话，不难
    def Merge(self, pHead1, pHead2):
        # write code here
        ans = ListNode(0)
        p = ans
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                p.next = pHead1
                pHead1 = pHead1.next
                p = p.next
            elif pHead1.val > pHead2.val:
                p.next = pHead2
                pHead2 = pHead2.next
                p = p.next
            else:
                p.next = pHead1
                pHead1 = pHead1.next
                p = p.next
                p.next = pHead2
                pHead2 = pHead2.next
                p = p.next
        while pHead1:
            p.next = pHead1
            pHead1 = pHead1.next
            p = p.next
        while pHead2:
            p.next = pHead2
            pHead2 = pHead2.next
            p = p.next
        return ans.next