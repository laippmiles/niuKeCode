'''
题目描述
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root is None:
            return []
            #注意特殊情况
        ans = []
        q = []
        p = root
        q.append(p)
        while q:
            p = q.pop(0)
            #靠堆栈实现逐层遍历
            ans.append(p.val)
            if p.left :
                q.append(p.left)
            if p.right :
                q.append(p.right)
        return ans