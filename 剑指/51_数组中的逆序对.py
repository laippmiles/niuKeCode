'''
题目描述
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。
即输出P%1000000007

输入描述:
题目保证输入的数组中没有的相同的数字

数据范围：
1.对于%50的数据,size<=10^4
2.对于%75的数据,size<=10^5
3.对于%100的数据,size<=2*10^5

示例1
输入
1,2,3,4,5,6,7,0
输出
7
'''
# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        count = self.mergeSort(data, 0)[1]
        #注意mergeSort输出的两个参数，本题用后者即可
        return count % 1000000007

    def mergeSort(self, nums, count):
        #其实就是归并排序的变体，重点在弄清楚在哪加逆序对的值
        if len(nums) <= 1:
            return nums, 0
        mid = len(nums) // 2
        #用递归先统计子数组内的逆序对，在归并统计
        #重点是递归思想
        left, count1 = self.mergeSort(nums[:mid], count)
        right, count2 = self.mergeSort(nums[mid:], count)
        #left，right输出来时已经是排好序的了
        count += count1 + count2
        ans = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                ans.append(left[i])
                i += 1
            else:
                ans.append(right[j])
                #如果right[j]比left[i]小
                #那left里left[i]往后的元素都比right[j]大，可以各自组成逆序对
                j += 1
                count += len(left) - i
        ans += left[i:]
        ans += right[j:]
        return ans, count