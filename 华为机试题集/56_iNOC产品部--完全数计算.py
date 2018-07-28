'''
题目描述
完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。

它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。

例如：28，它有约数1、2、4、7、14、28，除去它本身28外，
其余5个数相加，1+2+4+7+14=28。

给定函数count(int n),用于计算n以内(含n)完全数的个数。
计算范围, 0 < n <= 500000

返回n以内完全数的个数。 异常情况返回-1

/**

 *
 *  完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。

 *  它所有的真因子（即除了自身以外的约数）的和（即因子函数），
    恰好等于它本身。

 *  例如：28，它有约数1、2、4、7、14、28，
    除去它本身28外，其余5个数相加，1+2+4+7+14=28。

 *
 *  给定函数count(int n),用于计算n以内(含n)完全数的个数
 * @param n  计算范围, 0 < n <= 500000
 * @return n 以内完全数的个数, 异常情况返回-1
 *
 */
public   static   int  count( int  n)

输入描述:
输入一个数字

输出描述:
输出完全数的个数

示例1
输入
1000

输出
3
'''


def PerfectNumber(n):
    count = 1
    for i in range(2, int(n ** 0.5 + 1)):
        #注意象限
        if n % i == 0:
            count += i
            count += (n / i)
    if count == n:
        return 1
    else:
        return 0
    #完美数判断leetcode里写过

def count(n):
    if n < 2:
        print(-1)
    else:
        ans = 0
        for i in range(2, n):
            ans += PerfectNumber(i)
        print(ans)
    #老实人算法，挨个试是不是完美数

while True:
    try:
        n = int(input())
        count(n)
    except:
        break
