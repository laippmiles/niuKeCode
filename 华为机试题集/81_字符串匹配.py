'''
题目描述
题目标题：
判断短字符串中的所有字符是否在长字符串中全部出现

详细描述：
接口说明

原型：
boolIsAllCharExist(char* pShortString,char* pLongString);

输入参数：

    char* pShortString：短字符串

    char* pLongString：长字符串

输入描述:
输入两个字符串。第一个为短字符，第二个为长字符。

输出描述:
返回值：

示例1
输入
bc
abc
输出
true
'''
def func(a,b):
    for i in a:
        if i in b:
            continue
        else:
            return 'false'
    return 'true'
#这道题好像不需要考虑重复字母的状况
while True:
    try:
        a = input()
        b = input()
        print(func(a,b))
    except:
        break