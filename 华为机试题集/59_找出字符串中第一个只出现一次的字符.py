'''
题目描述
找出字符串中第一个只出现一次的字符

输入描述:
输入一个非空字符串

输出描述:
输出第一个只出现一次的字符，如果不存在输出-1

示例1
输入
asdfasdfo

输出
o
'''
def func(s):
    dicn = {}
    for i in s:
        if i not in dicn:
            dicn[i] = 1
        else:
            dicn[i] +=1
    dicn =sorted(dicn.items(),key = lambda x : s.index(x[0]))
    for i in dicn:
        if i[1] == 1:
            return i[0]
    return -1
    #哈希表+排序
while True:
    try:
        s = input()
        print(func(s))
    except:
        break