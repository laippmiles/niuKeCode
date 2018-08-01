'''
题目描述
正整数A和正整数B 的最小公倍数是指 能被A和B整除的最小的正整数值，
设计一个算法，求输入A和B的最小公倍数。

输入描述:
输入两个正整数A和B。

输出描述:
输出A和B的最小公倍数。

示例1
输入
5
7

输出
35

'''

#最小公倍数 = 两数之积除以最大公约数
#记得上面这句话即可
n = input().split()
a = int(n[0])
b = int(n[-1])
count = 1
gongbeishu = 1
while count <= min([a,b]):
    if a%count == 0 and b%count == 0:
        gongbeishu = count
    count += 1
print(int(a*b/gongbeishu))