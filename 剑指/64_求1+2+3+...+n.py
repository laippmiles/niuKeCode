'''
题目描述
求1+2+3+...+n，
要求不能使用乘除法、
不能使用for、while、if、else、switch、case等关键字
不能使用条件判断语句（A?B:C）。
'''
from functools import reduce
#python2是可以直接reduce的，python这个函数被移到functools库里了
# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        def f(x,y):
            return x+y
        return reduce(f,range(1,n+1))
    #python特产，reduce函数，好的，世界和平
