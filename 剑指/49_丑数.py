'''
题目描述
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。
 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''
'''
剑指的说法，这道题有点只可意会不可言传
思路二：创建数组保存已找到的丑数，用空间换时间的解法
 
试着找到一种只要计算丑数的方法，而不在非丑数的整数上浪费时间。
根据丑数的定义， 丑数应该是另一个丑数乘以2、3或者5的结果（1除外）。
因此我们可以创建一个数组，里面的数字是排好序的丑数，
每一个丑数都是前面的丑数乘以2、3或者5得到的。

这种思路的关键在于怎样确保数组里面的丑数是排好序的。
假设数组中已经有若干个丑数排好序后放在数组中，并且把已有最大的丑数记做M，
我们接下来分析如何生成下一个丑数。
该丑数肯定是前面某一个丑数乘以2、3或者5的结果，
所以我们首先考虑把已有的每个丑数乘以2。

在乘以2的时候，可以得到多干个小于等于M的结果。
由于是按顺序生成的，小于或者等于M肯定已经在数组中了，我们不需要再考虑；
还会得到若干个大于M的结果，但我们只需要第一个大于M的结果，
因为我们希望丑数是按照从小到大的顺序生成的，其他更大的结果以后再说。
我们把得到的第一个乘以2后大于M的丑数记为M2。

同样，我们把已有的每一个丑数乘以3和5，能得到第一个大于M的结果M3和M5。

那么下一个丑数应该是M2、M3和M5这三个数的最小者了 。

前面分析的时候，提到把已有的丑数分别乘以2、3和5。
事实上这不是必须的，因为已有的丑数是按照顺序放在数组中的。
对乘以2而言，肯定存在某一个丑数T2，
排在它之前的每一个乘以2得到的结果都会小于已有最大的丑数，
在它之后的每一个丑数乘以2得到的结果都会太大。

我们只需要记下这个丑数的位置，同时每次生成新的丑数的时候，取更新这个T2.
对于乘以3和5而言，也存在着同样的T3和T5。 
'''
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return 0
        ans = [1]
        index2 = 0
        index3 = 0
        index5 = 0
        for i in range(index-1):
            newNum = min([ans[index2]*2 , ans[index3]*3 ,ans[index5]*5])
            #基于从0开始的index2、index3、index5
            #从0开始每次加一个最小的数进数组，这样数组天生是排序的
            ans.append(newNum)
            if newNum % 2 == 0:
                index2 += 1
            #如果新加的数是2、3、5其中一个的倍数，相应index就可以+1找下一个相应倍数了
            if newNum % 3 == 0:
                index3 += 1
            if newNum % 5 == 0:
                index5 += 1
        return ans[-1]