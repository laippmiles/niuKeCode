# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        tmp = 1
        n = len(A)
        ans = []
        for i in range(n):
            tmp *= A[i]
            ans.append(tmp)
        return tmp

a = Solution()
print(a.multiply([1,2,3,4,5]))