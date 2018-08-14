'''
题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
'''
# -*- coding:utf-8 -*-
class Solution:
    #每个数的根节点肯定是最后一个元素
    #往左全是小于根节点的是左支
    #只要右支没有小于根节点的数就是搜索二叉树了
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        if len(sequence) == 1:
            return True
        n = len(sequence)
        root = sequence[-1]
        m = 0
        for i in range(n - 1):
            m = i
            if sequence[i] > root and len(sequence) > 2:
                break
        if m == n-2:
            m += 1

        #while sequence[m] < root:
            #m += 1
        #上面那个for循环用while更快
        #while可以覆盖没有右支的情况
        for j in range(m, n - 1):
            if sequence[j] < root and len(sequence) > 2:
                return False

        left = True
        if m > 0:
            left = self.VerifySquenceOfBST(sequence[:m])
            #递归考察左支情况

        right = True
        if m < n - 1:
            right = self.VerifySquenceOfBST(sequence[m:n - 1])
            #递归考察右支情况

        if left and right:
            return True
        else:
            return False
