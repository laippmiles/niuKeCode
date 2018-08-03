'''
题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''

# -*- coding:utf-8 -*-
#https://blog.csdn.net/iyuanshuo/article/details/79646899
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        l = 0
        r = len(rotateArray)-1
        if r < 0:
            return 0
        if r == 0:
            return rotateArray[0]
        while l <= r:
            mid = (l+r) // 2
            if r - l == 1:
                return rotateArray[r]
            #l,r差1的时候，二分法没办法继续，这时输出右边数据就好
            if rotateArray[l] == rotateArray[mid] and rotateArray[mid] == rotateArray[r]:
                #有种操蛋的特殊情况，l,r,mid三者都相同时，可能会使二分查找失效
                #这时换回顺序查找
                tep = rotateArray[l]
                for i in range(l,r+1):
                    if rotateArray[i] < tep :
                        tep = rotateArray[i]
                return tep
            if rotateArray[mid] >= rotateArray[l]:
                l = mid
            elif rotateArray[mid] <= rotateArray[r]:
                r = mid
        return rotateArray[r]