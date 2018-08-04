'''
题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

# -*- coding:utf-8 -*-
#右上角往左上角查找
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        row = len(array)
        col = len(array[0])
        rowi = 0
        coli = col - 1
        while rowi <= row-1 and coli >= 0:
            if array[rowi][coli] == target:
                return True
            if array[rowi][coli] > target:
                coli -= 1
            if array[rowi][coli] < target:
                rowi += 1
        return False