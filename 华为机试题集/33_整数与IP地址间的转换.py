'''
题目描述
原理：ip地址的每段可以看成是一个0-255的整数，
把每段拆分成一个二进制形式组合起来，然后把这个二进制数转变成一个长整数。

举例：一个ip地址为10.0.3.193
每段数字             相对应的二进制数
10                   00001010
0                    00000000
3                    00000011
193                  11000001
组合起来即为：00001010 00000000 00000011 11000001,
转换为10进制数就是：167773121，即该IP地址转换后的数字就是它了。

ip的每段可以看成是一个0-255的整数，需要对IP地址进行校验

输入描述:
输入
1 输入IP地址
2 输入10进制型的IP地址

输出描述:
输出
1 输出转换成10进制的IP地址
2 输出转换后的IP地址

输入
10.0.3.193
167969729

输出
167773121
10.3.3.193
'''
#没啥好说的，看图说话
def ip2int(s):
    lists = s.split('.')
    ans = ''
    for i in lists:
        tep = bin(int(i))[2:]
        add = '0'*(8 - len(tep)) + tep
        ans += add
    return int(ans,2)

def int2ip(num):
    tep = bin(int(num))[2:]
    ip = '0'*(32-len(tep)) + tep
    ans = ''
    for i in range(4):
        ans += str(int(ip[i*8:(i+1)*8],2)) + '.'
    return ans[:-1]

while True:
    try:
        s1 = input()
        print(ip2int(s1))
        s2 = input()
        print(int2ip(s2))
    except:
        break