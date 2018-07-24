'''
题目描述
功能:输入一个正整数，按照从小到大的顺序输出它的所有质数的因子（如180的质数因子为2 2 3 3 5 ）
最后一个数后面也要有空格

详细描述：

函数接口说明：
public String getResult(long ulDataInput)

输入参数：
long ulDataInput：输入的正整数

返回值：
String

示例1：

输入
180

输出
2 2 3 3 5
'''

while True:
    try:
        num = int(input())
        #注意这里要int，否则啥都出不来的
        a = 2
        while num != 1:
            if num % a == 0:
                print(a,end = ' ')
                #注意这里end要设成' '，否则末尾自动换行
                num /= a
            else:
                a += 1
                #这么除下去就能找到所有质数了，原理很好懂，但是不好描述
    except:
        break