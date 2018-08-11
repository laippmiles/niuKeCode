'''
题目描述
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
平衡二叉树：左右深度差不过超过1
'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def treeDepth(self, pRoot):
        if pRoot == None:
            return 0
        lDepth = self.treeDepth(pRoot.left)
        rDepth = self.treeDepth(pRoot.right)
        return max([lDepth, rDepth]) + 1

    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot is None:
            return True
        l = self.treeDepth(pRoot.left)
        r = self.treeDepth(pRoot.right)
        if abs(l - r) <= 1:
            return True
        else:
            return False

#结合55题做下去即可