'''
题目描述
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,
但是对于后面问题他就没辙了。
ACMer希望你们帮帮他,并把问题更加普遍化,
可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
'''
class Solution_example:
    def NumberOf1Between1AndN_Solution(self, n):
    #结合输出画图理解吧
    #自己举个例子统计一下
        # write code here
        res = 0
        tmp = n
        base = 1
        while tmp >= 1:
            #从个位开始，统计个、十、百以此类推从1-n中该位出现1的次数
            last = tmp % 10
            tmp = int(tmp/10)
            print('tmp:',tmp)
            print('tmp * base:',tmp * base)
            res += tmp * base
            print('n % base + 1:',n % base + 1)
            if last == 1:
                res += n % base + 1
            if last > 1:
                res += base
            print('base:',base)
            base *= 10
            #print('res:',res)
            #print('--------------')
        return res

# -*- coding:utf-8 -*-
#不行就死记硬背吧....
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        res = 0
        tmp = n
        base = 1
        while tmp >= 1:
            last = tmp % 10
            tmp = int(tmp/10)
            res += tmp * base
            if last == 1:
                res += n % base + 1
            if last > 1:
                res += base
            base *= 10
        return res

a = Solution_example()
b = a.NumberOf1Between1AndN_Solution(211)
print(b)