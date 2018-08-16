'''
题目描述
输入一个递增排序的数组和一个数字S，
在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。

输出描述:
对应每个测试案例，输出两个数，小的先输出。
'''# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        left = 0
        right = len(array)-1
        #定初值为两端的数
        while left < right:
            #到这有点像二分法了
            if array[left] + array[right] > tsum:
                right -= 1
            if array[left] + array[right] < tsum:
                left += 1
            if array[left] + array[right] == tsum:
                return [array[left],array[right]]
        return []
