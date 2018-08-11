# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if len(ss) == 0:
            return []
        if len(ss) == 1:
            return [ss]
        result = []
        temp = None
        for i in range(len(ss)):
            if ss[i] == temp:
                continue
            else:
                temp = ss[i]
            res = self.Permutation(ss[:i]+ss[i+1:])
            for j in res:
                result.append(ss[i]+j)
        return result