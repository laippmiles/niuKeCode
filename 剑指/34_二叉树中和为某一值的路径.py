'''
题目描述
输入一颗二叉树的跟节点和一个整数，
打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
(注意: 在返回值的list中，数组长度大的数组靠前)
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        #空节点返回[]
        if root and not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]
        #只有到了叶节点，正好符合要求的路径会被保存，否则都是空节点
        res = []
        left = self.FindPath(root.left,expectNumber-root.val)
        right = self.FindPath(root.right,expectNumber-root.val)
        for i in left+right:
            #left+right如果没找到路径，是个空列表，不会进循环的
            res.append([root.val]+i)
        return res