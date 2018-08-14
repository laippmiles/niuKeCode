'''
题目描述
输入两个整数序列，第一个序列表示栈的压入顺序，
请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，
序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
'''
# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        while len(pushV) != 0:
            stack.append(pushV.pop(0))
            #自己手写一次更好理解
            #这玩意很难描述啊
            #要用一个辅助栈重新让pushV入栈，再看能不能在这个过程里popV能全部出栈
            #popV能全出栈就行了，善用pop()
            while len(stack) != 0 and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        if len(popV) == 0:
            print(popV)
            print(stack)
            return True
        else:
            print(popV)
            print(stack)
            return False


a = Solution()
print(a.IsPopOrder([1,2,3,4,5],[4,5,3,2,1]))