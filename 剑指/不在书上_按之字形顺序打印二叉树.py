'''
题目描述
请实现一个函数按照之字形打印二叉树，
即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，
第三行按照从左到右的顺序打印，其他行以此类推。
'''
#和把二叉树打印成多行其实很像
#只需要加个Flag交替正逆序录入每一行即可
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        ans = []
        if not pRoot:
            return ans
        stack = [pRoot]
        Flag = True
        while len(stack) != 0:
            n = len(stack)
            row = []
            for i in stack:
                row.append(i.val)
            if Flag:
                ans.append(row)
                Flag = False
            else:
                ans.append(row[::-1])
                Flag = True
            for j in range(n):
                p = stack.pop(0)
                if p.left:
                    stack.append(p.left)
                if p.right:
                    stack.append(p.right)
        return ans