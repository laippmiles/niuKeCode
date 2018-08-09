# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        ans = []
        lenN = len(num)
        if size > lenN:
            return ans
        ans.append(max(num[:size]))
        n = 1
        while n+size <= lenN:
            ans.append(max(num[n:n+size]))
            n += 1
        return ans

a = Solution()
print(a.maxInWindows([2,3,4,2,6,2,5,1],3))