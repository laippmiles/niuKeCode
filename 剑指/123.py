# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root is None:
            return None
        ans = []
        q = []
        p = root
        q.append(p)
        while q:
            p = q.pop(0)
            ans.append(p.val)
            if p.left :
                q.append(p.left)
            if p.right :
                q.append(p.right)
        return ans