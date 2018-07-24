'''
题目描述
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。
如果小数点后数值大于等于5,向上取整；小于5，则向下取整。

输入描述:
输入一个正浮点数值

输出描述:
输出该数值的近似整数值

示例1

输入
5.5

输出
6
'''
while True:
    try:
        n = float(input())
        #注意这里要用float，int是不转字符串→小数的
        if (n - int(n)) >= 0.5:
            print (int(n+1))
        else:
            print(int(n))
    except:
        break