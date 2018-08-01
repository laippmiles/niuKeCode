'''
题目描述
如果统计的个数相同，则按照ASCII码由小到大排序输出 。
如果有其他字符，则对这些字符不用进行统计。

实现以下接口：
输入一个字符串，对字符中的各个英文字符，数字，空格进行统计（可反复调用）
按照统计个数由多到少输出统计结果，如果统计的个数相同，
则按照ASII码由小到大排序输出

清空目前的统计结果，重新统计
调用者会保证：
输入的字符串以‘\0’结尾。



输入描述:
输入一串字符。

输出描述:
对字符中的
各个英文字符（大小写分开统计），数字，空格进行统计，
并按照统计个数由多到少输出,如果统计的个数相同，则按照ASII码由小到大排序输出 。

如果有其他字符，则对这些字符不用进行统计。

示例1
输入
aadddccddc

输出
dca
'''

while True:
    try:
        s = input()
        dicn={}
        for i in s:
            if i.isdigit() or i.isalpha() or i ==' ':
                if i not in dicn:
                    dicn[i] = 1
                else:
                    dicn[i] += 1
        dicn = sorted(dicn.items(), key=lambda x1: (-x1[1], x1[0]))
        #主要在这个二次排序里
        #key可以按冒号后的元祖顺序的优先级排序的
        #主要是逆序只能用数字相关的，正序的字典排序还能用
        ans = ''
        for i in dicn:
            ans += i[0]
        print(ans)
    except:
        break