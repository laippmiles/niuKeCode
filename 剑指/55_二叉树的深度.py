'''
题目描述
输入一棵二叉树，求该树的深度。
从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，
最长路径的长度为树的深度。
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot is None:
            #递归停止条件：遍历到最底下
            return 0
        lDepth = self.TreeDepth(pRoot.left)
        rDepth = self.TreeDepth(pRoot.right)
        return max([lDepth,rDepth]) + 1