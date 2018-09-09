'''
pucExpression字符串中的有效字符包括
[‘0’-‘9’],‘+’,‘-’, ‘*’,‘/’ ,‘(’， ‘)’,‘[’, ‘]’,‘{’ ,‘}’。

pucExpression算术表达式的有效性由调用者保证;

输入
3+2*{1+2*[-4/(8-6)+7]}

输出
25
'''

while True:
    try:
        s = input()
        print(eval(s))
    except:
        break

#python的eval可以转表达式，认中括号和大括号
#比eval还牛逼的是exec，可以动态执行python代码。
#也就是说exec可以执行复杂的python代码，而不像eval函数那样只能计算一个表达式的值。