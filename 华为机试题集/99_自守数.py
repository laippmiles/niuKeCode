'''
题目描述
自守数是指一个数的平方的尾数等于该数自身的自然数。
例如：25^2 = 625，76^2 = 5776，9376^2 = 87909376。
请求出n以内的自守数的个数


接口说明
/*
功能: 求出n以内的自守数的个数
输入参数：
int n

返回值：
n以内自守数的数量。
*/
public static int CalcAutomorphicNumbers( int n)
{
/*在这里实现功能*/
return 0;
}

输入描述:
int型整数

输出描述:
n以内自守数的数量。

示例1
输入
2000

输出
8
'''

def CalcAutomorphicNumbers(n):
    s = str(n)
    if str(n**2)[-len(s):] == s:
        return 1
    else:
        return 0

#暴力法，挨个分析，时间够用
while True:
    try:
        n = int(input())
        ans = 0
        for i in range(n):
            ans += CalcAutomorphicNumbers(i)

        print(ans)
    except:
        break