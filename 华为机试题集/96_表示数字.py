'''
题目描述
将一个字符中所有出现的数字前后加上符号“*”，其他字符保持不变
 public static String MarkNum(String pInStr)
 {

  return null;
 }
输入描述:
输入一个字符串

输出描述:
字符中所有出现的数字前后加上符号“*”，其他字符保持不变

输入
Jkdi234klowe90a3
输出
Jkdi*234*klowe*90*a*3*
'''

while True:
    try:
        s = input()
        num = ''
        ans = ''
        for i in s:
            if not i.isdigit():
                if num != '':
                    num += '*'
                    ans += num
                    num = ''
                ans += i
            else:
                if num == '':
                    num += '*'
                num += i
        if num != '':
            num += '*'
            ans += num
        print(ans)
    except:
        break