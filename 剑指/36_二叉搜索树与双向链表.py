'''
题目描述
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def listRes(self, pRootOfTree):
        if not pRootOfTree:
            return []
        return self.listRes(pRootOfTree.left) + [pRootOfTree] + self.listRes(pRootOfTree.right)
        #先用一个数组按中序遍历把树节点存起来，因为是二叉搜索树，中序遍历后数组是排序的
        #二叉搜索树：左节点的值不大于根节点的值，右节点的值不小于根节点的值
    def Convert(self, pRootOfTree):
        # write code here
        res = self.listRes(pRootOfTree)
        if len(res) == 0:
            return None
        if len(res) == 1:
            return pRootOfTree
        res[0].left = None
        res[0].right = res[1]

        res[-1].right = None
        res[-1].left = res[-2]
        #数组首末两端的节点需要特殊处理

        for i in range(1, len(res) - 1):
            res[i].left = res[i - 1]
            res[i].right = res[i + 1]
            #其余节点对应修改左右关系即可
        return res[0]
        #只输出头结点