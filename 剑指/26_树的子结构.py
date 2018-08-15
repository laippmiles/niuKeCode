'''
题目描述
输入两棵二叉树A，B，判断B是不是A的子结构。
（ps：我们约定空树不是任意一个树的子结构）
'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        return self.is_subTree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right,pRoot2)

    def is_subTree(self, pRoot1, pRoot2):
        if not pRoot2:
            return True
        #注意先判断pRoot2是不是已经到叶节点了，如果是，意味着找到了子结构
        if not pRoot1 or pRoot1.val != pRoot2.val:
            return False
        return self.is_subTree(pRoot1.left, pRoot2.left) and self.is_subTree(pRoot1.right, pRoot2.right)

#这道题考递归，照思路写就行