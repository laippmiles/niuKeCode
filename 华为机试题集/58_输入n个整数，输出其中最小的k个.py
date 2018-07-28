'''
题目描述
输入n个整数，输出其中最小的k个。

详细描述：
接口说明

原型：
bool GetMinK(unsignedint uiInputNum, int * pInputArray, unsignedint uiK, int * pOutputArray);

输入参数：
unsignedint uiInputNum //输入整数个数
int * pInputArray  //输入整数数组
unsignedint uiK   //需输出uiK个整数

输出参数（指针指向的内存区域保证有效）：
int * pOutputArray //最小的uiK个整数

返回值：

false 异常失败
true  输出成功

输入描述:
输入说明
1 输入两个整数
2 输入一个整数数组

输出描述:
输出一个整数数组

示例1
输入
5 2
1 3 5 7 2

输出
1 2
'''

#主要注意处理的数据是int还是str，别的就是排序了
while True:
    try:
        a = input().split()
        num = int(a[0])
        k = int(a[-1])
        num = input().split()
        for i in range(len(num)):
            num[i] = int(num[i])
        num.sort()
        ans = ''
        for i in range(k):
            ans += str(num[i])
            ans += ' '
        print(ans[:-1])
    except:
        break