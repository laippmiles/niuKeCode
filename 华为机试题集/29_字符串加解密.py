'''
题目描述
1、对输入的字符串进行加解密，并输出。

2加密方法为：

当内容是英文字母时则用该英文字母的后一个字母替换，
同时字母变换大小写,如字母a时则替换为B；字母Z时则替换为a；

当内容是数字时则把该数字加1，如0替换1，1替换2，9替换0；

其他字符不做变化。

3、解密方法为加密的逆过程。

接口描述：

实现接口，每个接口实现1个基本操作：

void Encrypt (char aucPassword[], char aucResult[])：
在该函数中实现字符串加密并输出

说明：
1、字符串以\0结尾。
2、字符串最长100个字符。

int unEncrypt (char result[], char password[])：
在该函数中实现字符串解密并输出

说明：
1、字符串以\0结尾。
2、字符串最长100个字符。

输入描述:
输入说明
输入一串要加密的密码
输入一串加过密的密码

输出描述:
输出说明
输出加密后的字符
输出解密后的字符

输入
abcdefg
BCDEFGH

输出
BCDEFGH
abcdefg
'''

alp = 'abcdefghijklmnopqrstuvwxyz'

def encode(s):
    ans = ''
    for i in s:
        if i.isdigit():
            if int(i) == 9:
                ans += '0'
                continue
            else:
                ans += str(int(i) + 1)
                continue
        elif i.isalpha():
            if i == i.lower():
                if i == 'z':
                    ans += 'A'
                else:
                    ans += alp[alp.index(i) + 1].upper()
            else:
                if i == 'Z':
                    ans += 'a'
                else:
                    ans += alp[alp.index(i.lower()) + 1]
        else:
            ans += i
    return ans

def decode(s):
    ans = ''
    for i in s:
        if i.isdigit():
            if int(i) == 0:
                ans += '9'
                continue
            else:
                ans += str(int(i) - 1)
                continue
        elif i.isalpha():
            if i == i.lower():
                if i == 'a':
                    ans += 'Z'
                    continue
                else:
                    ans += alp[alp.index(i) - 1].upper()
            else:
                if i == 'z':
                    ans += 'A'
                else:
                    ans += alp[alp.index(i.lower()) - 1]
        else:
            ans += i
    return ans

#又是不while True就不输出的神奇问题
while True:
    try:
        s1 = input()
        s2 = input()
        print(encode(s1))
        print(decode(s2))
    except:
        break