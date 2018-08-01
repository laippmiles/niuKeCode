'''
题目描述
从输入任意个整型数，统计其中的负数个数并求所有非负数的平均值
输入描述:
输入任意个整数

输出描述:
输出负数个数以及所有非负数的平均值

示例1
输入
-13
-4
-7

输出
3
0.0
'''

l = list(map(int,input().split()))
count = 0
countp = 0
ans = 0
for i in l:
    if i < 0 :
        count += 1
    else:
        countp += 1
        ans += i
print(count)
#%(ans/countp)要加括号
print('%0.1f'%(ans/countp))