'''
题目描述

请实现两个函数，分别用来序列化和反序列化二叉树
'''
# -*- coding:utf-8 -*-
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def __init__(self):
        self.index = -1
        self.l = None

    def Serialize(self, root):
        # write code here
        if not root:
            return '#'
            #None点用#标注
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)
        #递归输出二叉树的前序遍历序列

    def Deserialize(self, s):
        # write code here
        self.index += 1
        if self.index == 0:
            self.l = s.split(',')

        if self.index >= len(self.l):
            return None

        root = None
        if self.l[self.index] != '#':
            root = TreeNode(int(self.l[self.index]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
            #用递归的方法再把前序遍历序列变回树，之前树里None的标识可以起作用了
        return root
