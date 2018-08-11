'''
题目描述
操作给定的二叉树，将其变换为源二叉树的镜像。
输入描述:
二叉树的镜像定义：源二叉树
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root is None or (root.left == None and root.right == None):
            #递归结束条件：该点为空或该点为叶节点
            return
        tep = root.left
        root.left = root.right
        root.right = tep
        #结合递归左右倒置即可
        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)