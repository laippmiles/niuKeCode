'''
题目描述
给出一个名字，该名字有26个字符串组成，
定义这个字符串的“漂亮度”是其所有字母“漂亮度”的总和。
每个字母都有一个“漂亮度”，范围在1到26之间。
没有任何两个字母拥有相同的“漂亮度”。字母忽略大小写。
给出多个名字，计算每个名字最大可能的“漂亮度”。

输入描述:
整数N，后续N个名字

输出描述:
每个名称可能的最大漂亮程度

示例1
输入
2
zhangsan
lisi

输出
192
101
'''

#频数最高的字母取最大漂亮度，以此类推即可
def func(s):
    dicn = {}
    for i in s :
        if i not in dicn:
            dicn[i] = 1
        else:
            dicn[i] += 1
    dicn = sorted(dicn.items(),key = lambda x : x[1],reverse = True)
    count = 0
    val = 26
    for j in dicn:
        count += j[1]*val
        val -= 1
    return count

while True:
    try:
        num = int(input())
        for i in range(num):
            s = input()
            print(func(s))
    except:
        break
