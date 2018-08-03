'''
题目描述
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
'''

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        l = []
        while listNode is not None:
            #遍历一个链表的必备步骤
            l.append(listNode.val)
            listNode = listNode.next
            #更新到下一个链表的必备步骤
        return l[::-1]