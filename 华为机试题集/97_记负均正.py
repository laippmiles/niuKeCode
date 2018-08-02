'''
题目描述
首先输入要输入的整数个数n，然后输入n个整数。
输出为n个整数中负数的个数，和所有正整数的平均值，结果保留一位小数。

输入描述:
首先输入一个正整数n，
然后输入n个整数。

输出描述:
输出负数的个数，和所有正整数的平均值。

示例1
输入
5
1
2
3
4
5
输出
0 3
'''

while True:
    try:
        n = int(input())
        num = list(map(int,input().split()))
        count = 0
        countp = 0
        sumn = 0
        for i in num:
            if i < 0 :
                count += 1
            elif i > 0:
                countp += 1
                sumn += i
        print(count,end = ' ')
        if countp != 0:
            #这里记得加个条件，要不没有正数的时候会崩溃的
            print('%.1f'%(sumn/countp))
        else:
            print(0)
    except:
        break