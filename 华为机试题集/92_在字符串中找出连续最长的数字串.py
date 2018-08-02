'''
题目描述
样例输出
输出123058789，函数返回值9
输出54761，函数返回值5


接口说明
函数原型：
   unsignedint Continumax(char** pOutputstr,  char* intputstr)

输入参数：
   char* intputstr  输入字符串；

输出参数：
   char** pOutputstr: 连续最长的数字串，如果连续最长的数字串的长度为0，
   应该返回空字符串；如果输入字符串是空，也应该返回空字符串；

返回值：
  连续最长的数字串的长度

输入描述:
输入一个字符串。

输出描述:
输出字符串中最长的数字字符串和它的长度。
如果有相同长度的串，则要一块儿输出，但是长度还是一串的长度

输入
abcd12345ed125ss123058789
输出
123058789,9
'''

while True:
    try:
        num =''
        ans = ''
        count = 0
        s = input()
        for i in s:
            if i.isdigit():
                num += i
            else:
                if len(num) > count:
                    count = len(num)
                    ans = num
                elif len(num) == count:
                    #如果有相同长度的串，则要一块儿输出，但是长度还是一串的长度
                    #注意这句话
                    ans += num
                num = ''
        if len(num) > count:
                    count = len(num)
                    ans = num
        elif len(num) == count:
                    ans += num
        print(ans+','+str(count))
    except:
        break