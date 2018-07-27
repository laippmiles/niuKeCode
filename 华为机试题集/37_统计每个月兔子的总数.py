'''
题目描述
有一只兔子，从出生后第3个月起每个月都生一只兔子，
小兔子长到第三个月后每个月又生一只兔子，假如兔子都不死，
问每个月的兔子总数为多少？

/**
 * 统计出兔子总数。
 *
 * @param monthCount 第几个月
 * @return 兔子总数
 */
public static int getTotalCount(int monthCount)
{
    return 0;
}

输入描述:
输入int型表示month

输出描述:
输出兔子总数int型

输入
9

输出
34
'''

#本题有参考：
#https://www.nowcoder.com/questionTerminal/1221ec77125d4370833fd3ad5ba72395

def getTotalCount(s):
    month1 = 1
    #记录目前1月龄兔数目
    month2 = 0
    #记录目前2月龄兔数目
    month3 = 0
    #记录目前3月龄(能生)兔数目
    while s > 1:
        #这里不能写 >0，要不会多计算一轮的
        month3 += month2
        month2 = month1
        month1 = month3
        s -= 1
        #又是看图说话了
    print(month3 + month2 + month1)


while True:
    try:
        s = int(input())
        getTotalCount(s)
    except:
        break