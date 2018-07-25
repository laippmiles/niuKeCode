'''

题目描述
开发一个简单错误记录功能小模块，能够记录出错的代码所在的文件名称和行号。

处理：
1、 记录最多8条错误记录，循环记录，
    对相同的错误记录（净文件名称和行号完全匹配）只记录一条，错误计数增加；
2、 超过16个字符的文件名称，只记录文件的最后有效16个字符；
3、 输入的文件可能带路径，记录文件名称不能带路径。

输入描述:
一行或多行字符串。每行包括带路径文件名称，行号，以空格隔开。

输出描述:
将所有的记录统计并将结果输出，格式：文件名 代码行数 数目，一个空格隔开，如：

示例1
输入
E:\V1R2\product\fpgadrive.c   1325
输出
fpgadrive.c 1325 1
'''
ans = []
while True:
    #记录最多8条错误记录，循环记录
    #注意这句话，所以要用while True
    try:
        s = input().split(' ')
        hangshu = int(s[-1])
        lujing = s[0].split('\\')[-1]
        if len(lujing) > 16:
            lujing = lujing[-16:]
        add = [lujing,hangshu,1]
        if len(ans) == 0:
            ans.append(add)
        else:
            Flag = True
            for i in ans:
                if i[0] == add[0] and i[1] == add[1]:
                    i[2] += 1
                    Flag = False
            if Flag:
                ans.append(add)
    except:
        break
for i in ans[-8:]:
    print(i[0]+' '+str(i[1])+' '+str(i[2]))