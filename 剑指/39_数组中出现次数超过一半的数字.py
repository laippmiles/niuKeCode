'''
题目描述
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。
如果不存在则输出0。
'''

# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if len(numbers) == 0:
            return 0
        elif len(numbers) == 1:
            return numbers[0]
        #处理特殊情况
        div = int(len(numbers)/2)
        lastInd = len(numbers)-1
        numbers[div],numbers[lastInd] = numbers[lastInd],numbers[div]
        #将中间的数先交换到末尾，接下来就是按快速排序的一个步骤来即可
        i = -1
        for j in range(len(numbers)-1):
            if numbers[j] <= numbers[lastInd]:
                i += 1
                numbers[i],numbers[j] = numbers[j],numbers[i]
        numbers[i+1],numbers[lastInd] = numbers[lastInd],numbers[i+1]
        if numbers.count(numbers[div+1]) > (lastInd+1)/2:
            #标准数在div+1索引，要注意这点
            return numbers[div+1]
        else:
            return 0