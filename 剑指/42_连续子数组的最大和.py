'''
题目描述
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。
今天测试组开完会后,他又发话了:
在古老的一维模式识别中,常常需要计算连续子向量的最大和,
当向量全为正数的时候,问题很好解决。
但是,如果向量中包含负数,是否应该包含某个负数,
并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},
连续子向量的最大和为8(从第0个开始,到第3个为止)。

给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？
(子向量的长度至少是1)
'''

#参考：
#https://blog.csdn.net/u010636181/article/details/78422169
# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        ans = []
        sumn = 0
        for i in range(len(array)):
            #设一个ans列表，保存到第i位为止可能最高的连续字数和
            if i == 0 or sumn >= 0:
                sumn += array[i]
                #如果前面的和大于零或者开局时
                #该位子数组和记为前面的和加第i个元素
            else:
                sumn = array[i]
                #如果前面的子和小于零，重置子和，只记第i个元素
            ans.append(sumn)
            #依次记录
        return max(ans)
        #ans里的最大值即为所求