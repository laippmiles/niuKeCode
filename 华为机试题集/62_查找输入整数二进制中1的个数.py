'''
题目描述
请实现如下接口
 public   static   int  findNumberOf1( int num)

{
     /*  请实现  */
     return  0;
} 譬如：输入5 ，5的二进制为101，输出2


输入描述:
输入一个整数

输出描述:
计算整数二进制中1的个数

示例1
输入
5

输出
2
'''

#python标准入门题
while True:
    try:
        s = int(input())
        s = bin(s)[2:]
        count = 0
        for i in s:
            if i == '1':
                count += 1
        print(count)
    except:
        break