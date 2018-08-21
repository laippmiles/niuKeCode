'''
在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。

注意:
n 是正数且在32为整形范围内 ( n < 231)。

示例 1:

输入:
3
输出:
3
'''

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        base = 1
        #初始设位数为1
        count = 9
        #初始设所有i位数含count个数字
        tep = 0
        #记录i-1位数所含的数字数
        while count < n:
            #用这个循环确定第n个数字在几位数里
            base += 1
            tep = count
            count += 9 * (10**(base-1))*base
        #在找到的第base位数里继续找第n位的确切位置
        n -= tep
        a = n / base
        #a用来确定n在哪个数字里
        b = n % base
        #b用来确定n在某数字的第几位
        if b == 0:
            return int(str(10 ** (base-1) + a - 1)[-1])
        else:
            return int(str(10 ** (base-1) + a)[b-1])

        #
        #举例第n=12时
        #base = 1 ， tep = 0 ，count = 9 * (10**(base-1))*base = 9
        #9<12，继续
        #base = 2 ， tep = 9 ，count += 9 * (10**(base-1))*base = 189
        #189>12，确定在二位数找n
        #n -= tep ,n = 3 , 找二位数里排第3的数
        #a = n / base ，a = 1
        #b = n % base ,b = 1
        #二位数从10起头，因此答案为10 + a 这个数的第b个数字