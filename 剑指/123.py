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
    print(stack1)
    print(stack2)
    i = 1
    j = 0
    while i < len(stack1) and j < len(stack2):
        if stack2[j] >= stack1[i]:
            del stack2[j]
            del stack1[i]
            print(stack1)
            print(stack2)
        else:
            i += 1
            j += 1