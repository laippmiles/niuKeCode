'''
题目描述
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,
则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
'''
# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        if ss == '':
            return []
        elif len(ss) == 1:
            return [ss]
        result = []
        temp = None
        for i in range(len(ss)):
            if ss[i] == temp:
                continue
                #如果是连续两个同样的字母，就不需要再重复走下面的递归了
            else:
                temp = ss[i]
            res = self.Permutation(ss[:i]+ss[i+1:])
            #递归全排列除了该字母外的字符串
            for j in res:
                result.append(ss[i]+j)
                #全排列完了以后该织字母放顶头即可
        return result