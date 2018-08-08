'''
题目描述
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，
但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的库函数。
 数值为0或者字符串不是一个合法的数值则返回0。

输入描述:
输入一个字符串,包括数字字母符号,可以为空
输出描述:
如果是合法的数值表达则返回该数字，否则返回0

示例1
输入
+2147483647
    1a33

输出
2147483647
    0
'''

# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        flag = True
        if len(s) == 0:
            return 0
        #特殊情况1，空值
        if s[0] == "+":
            if len(s) > 1:
                s = s[1:]
            #考虑输入'+'情况，下面'-'同理
            else:
                return 0
        if s[0] == '-':
            if len(s) > 1:
                s = s[1:]
                flag = False
                #加个符号标志位
            else:
                return 0
        for i in s:
            if i.isdigit():
                #这里就是看图说话了
                continue
            else:
                return 0
        if flag:
            return int(s)
        else:
            return int(s) * -1