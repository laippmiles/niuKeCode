'''
题目描述
输入整型数组和排序标识，
对其元素按照升序或降序进行排序（一组测试用例可能会有多组数据）

接口说明
原型：
void sortIntegerArray(Integer[] pIntegerArray, int iSortFlag);

输入参数：
Integer[] pIntegerArray：整型数组
int  iSortFlag：排序标识：0表示按升序，1表示按降序

输出参数：
无

返回值：
void


输入描述:
1、输入需要输入的整型数个数

输出描述:
输出排好序的数字

输入
8
1 2 4 9 3 55 64 25
0

输出
1 2 3 4 9 25 55 64
'''

#没啥好说的，python标准技能
while True:
    try:
        num = input()
        l = list(map(int,input().split()))
        flag = input()

        if flag == '0':
            l.sort()
        else:
            l.sort(reverse = True)

        ans = ''
        for i in l:
            ans += str(i)
            ans += ' '
        print(ans[:-1])
    except:
        break