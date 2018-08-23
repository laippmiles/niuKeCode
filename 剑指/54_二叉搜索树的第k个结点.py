'''
题目描述
给定一棵二叉搜索树，请找出其中的第k小的结点。
例如,(5，3，7，2，4，6，8)中，按结点数值大小顺序第三小结点的值为4。
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def midRead(self, pRoot):
        if not pRoot:
            return []
        return self.midRead(pRoot.left) + [pRoot] + self.midRead(pRoot.right)
        #因为是二叉搜索树，用中序遍历先遍历出来，遍历出来的数组就是排序的
        #取出第k个节点的节点即可

    def KthNode(self, pRoot, k):
        # write code here
        res = self.midRead(pRoot)
        if k == 0 or k > len(res):
            return None
        else:
            return res[k - 1]