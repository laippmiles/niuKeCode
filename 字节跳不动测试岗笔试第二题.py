'''
题目描述
为了提离文章鹿畺，每一篇文章（假设全部都是英文）都会有m名编辑审核。
每个编辑独立工作，会把觉得有问題的句子通过下标记录下来。
比如[1,10], 1表示病句的第一个字符, 10表示病句的最后一个字符。
也就是从1到10个宇符组成的句子，是有问题的。
现在需要把多名编辑觉得有问题的句子合并起来，送给总编辑进行最终的审核。
比如编辑指出的病句是[1,10]，[32,45]; B 编辑推出的病句 是[5,16], [78,94],
那么[1,10]和 [15,16]是有交叉的，可以合并成, [32,45], [78,94]

输入描述：
编辑数置m,之后每行是每个编辑的标记的下标集合。
第一个和最后一个下标用英文逗号分隔,每组下标之间用分号分隔开

输出描述：
合并后的下标集合，第一个和最后1下标用英文逗号分隔，
每且下标之间用分号分隔。返回结果是从小到大递增排列

输入:
3
1,10;32,45
78,94;5,16
80,100;200,220;16,32

输出：
1,45;78,100;200,220
'''

import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    stack1 = []
    stack2 = []
    for i in range(n):
        # 读取每一行
        line = input().split(';')
        # 把每一行的数字分隔后转化成int列表
        for i in line:
            stack1.append(int(i.split(',')[0]))
            stack2.append(int(i.split(',')[1]))
    stack1.sort()
    stack2.sort()
    i = 1
    j = 0
    while i < len(stack1) and j < len(stack2):
        if stack2[j] >= stack1[i]:
            del stack2[j]
            del stack1[i]
        else:
            i += 1
            j += 1
    for k in range(len(stack1)):
        if k == len(stack1) - 1:
            print(str(stack1[k])+','+str(stack2[k]))
        else:
            print(str(stack1[k])+','+str(stack2[k]),end = ';')
