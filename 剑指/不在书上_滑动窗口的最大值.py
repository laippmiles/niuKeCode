'''
题目描述
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，
那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}；
针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
{[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}，
 {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
'''

# -*- coding:utf-8 -*-
#直接窗口扫过去就是了
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        ans = []
        lenN = len(num)
        if size == 0:
            return []
        if size > lenN:
            return ans
        ans.append(max(num[:size]))
        n = 1
        while n+size <= lenN:
            ans.append(max(num[n:n+size]))
            n += 1
        return ans