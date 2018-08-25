'''
题目描述
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return []
        ans = []
        stack = [pRoot]
        while stack:
            row = []
            for i in stack:
                row.append(i.val)
            ans.append(row)
            #在这里写上层的节点数
            n = len(stack)
            for i in range(n):
                p = stack.pop(0)
                #这个是关键步骤
                if p.left:
                    stack.append(p.left)
                if p.right:
                    stack.append(p.right)
        return ans