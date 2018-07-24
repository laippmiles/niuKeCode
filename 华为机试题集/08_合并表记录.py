'''
题目描述
数据表记录包含表索引和数值，请对表索引相同的记录进行合并，
即将相同索引的数值进行求和运算，输出按照key值升序进行输出。

输入描述:
先输入键值对的个数
然后输入成对的index和value值，以空格隔开

输出描述:
输出合并后的键值对（多行）

输入
4
0 1
0 2
1 2
3 4

输出
0 3
1 2
3 4
'''

dicn = {}
num = int(input())
for i in range(num):
    a = input().split(' ')
    #这里注意split()输出不是None
    #要么接着往下写，要么a = a.split(' ')
    a[0] = int(a[0])
    a[1] = int(a[1])
    if a[0] in dicn:
        dicn[a[0]] += a[1]
    else:
        dicn[a[0]] = a[1]
n = sorted(dicn.items(), key = lambda x :x[0])
for i in n:
    print(str(i[0]) + ' ' + str(i[1]))