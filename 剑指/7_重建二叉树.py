'''
题目描述
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if pre is None or tin is None:
            return None
        if set(pre) - set(tin):
            #考虑非法输入
            return 'Error'

        #找到左右树的序列
        ind = tin.index(pre[0])

        if ind != 0:
            left_tin = tin[:ind]
            left_pre = pre[1:1 + ind]
        else:
            left_tin = None
            left_pre = None

        if ind != len(tin) - 1:
            right_tin = tin[ind + 1:]
            right_pre = pre[1 + ind:]
        else:
            right_tin = None
            right_pre = None

        root = TreeNode(pre[0])
        root.left = self.reConstructBinaryTree(left_pre, left_tin)
        root.right = self.reConstructBinaryTree(right_pre, right_tin)
        return root