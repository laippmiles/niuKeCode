'''
题目描述
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''

# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        #python2的cmp到3已经不能用了
        #所以涉及自定义函数的话记得用functools的cmp_to_key
        #用cmp_to_key转过以后用法和python2一致了
        from functools import cmp_to_key
        if len(numbers) == 0:
            return ''
        func = lambda n1,n2:int(str(n1)+str(n2))-int(str(n2)+str(n1))
        #func是自定义排序规则
        #规则内n1 > n2 输出一个正数
        #n1 < n2 输出一个负数
        numbers = sorted(numbers,key = cmp_to_key(func))
        return ''.join([str(i) for i in numbers])
        #答案最后用个推导式