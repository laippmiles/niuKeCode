'''
题目描述
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''
# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return pNode
        if pNode.right:
            #如果该节点有右支的话，答案是右支最左的节点
            ans = pNode.right
            while ans.left:
                ans = ans.left
            return ans
        else:
            #如果没有右支，往上遍历
            #答案的子节点是答案的左支
            ans = pNode
            while ans.next:
                if ans.next.left == ans:
                    return ans.next
                ans = ans.next
            return None