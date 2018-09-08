'''
题目描述
密码要求:

1.长度超过8位
2.包括大小写字母.数字.其它符号,以上四种至少三种
3.不能有相同长度超2的子串重复

说明:长度超过2的子串

输入描述:
一组或多组长度超过2的子符串。每组占一行

输出描述:
如果符合要求输出：OK，否则输出NG

示例1
输入
021Abc9000
021Abc9Abc1
021ABC9000
021$bc9000

输出
OK
NG
NG
OK
'''

def main(pw):
    if len(pw) <= 8:
        return False
    #检查长度
    for i in range(len(pw) - 3):
        if pw[i:i + 3] in pw[i + 3:]:
            return False
    #检查子字符串
    count = [0] * 4
    #用标记法检查是不是够3种
    for j in range(len(pw)):
        if 'a' <= pw[j] and 'z' >= pw[j]:
            count[0] = 1
        elif 'A' <= pw[j] and 'Z' >= pw[j]:
            count[1] = 1
        elif '0' <= pw[j] and '9' >= pw[j]:
            count[2] = 1
        else:
            count[3] = 1
        if sum(count) >= 3:
            #在这写个符合要求提前结束好像对性能有帮助
            return True
    if sum(count) < 3:
        return False
    return True

while True:
    try:
        pw = input()
        if main(pw):
            print('OK')
        else:
            print('NG')
    except:
        break
