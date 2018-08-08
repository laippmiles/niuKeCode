'''
题目描述
请实现一个函数，用来判断一颗二叉树是不是对称的。
注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            #not pRoot → pRoot is None
            return True
            #单独判断空数
        return self.func(pRoot.left, pRoot.right)

    def func(self, pRoot1, pRoot):
        if pRoot1 is None and pRoot is None:
            #先判断是不是同时是None
            return True
        if pRoot1 is None or pRoot is None:
            #再判断是不是有其中一个是None
            return False
        if pRoot1.val != pRoot.val:
            return False
        return self.func(pRoot1.left, pRoot.right) and self.func(pRoot1.right, pRoot.left)
        #递归判断子树
        #中序是左中右，判断镜像的参考是同时对照右中左