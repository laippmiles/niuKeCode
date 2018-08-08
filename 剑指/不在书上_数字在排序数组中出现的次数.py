'''
题目描述
统计一个数字在排序数组中出现的次数。
'''
# -*- coding:utf-8 -*-
class Solution:
    #用双指针比较快，注意处理好特殊情况即可
    def GetNumberOfK(self, data, k):
        # write code here
        right = len(data) - 1
        left = 0
        while left <= right:
            if data[left] == k and data[right] == k:
                break
            if data[left] < k:
                left += 1
            if data[right] > k:
                right -= 1

        if left == right:
            if data[left] == k:
                return 1
            else:
                return 0
        return right - left + 1