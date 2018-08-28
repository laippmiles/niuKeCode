def func(a):
    l = [0, 0]
    for i in b:
        if l[0] < int(i[0]):
            l[0] = int(i[0])
        if l[1] < int(i[1]):
            l[1] = int(i[1])
    return l

if __name__ == "__main__":
    T0 = int(input())
    b = []
    for i in range(T0):
        T = input().split()
        a = []
        for j in T:
            a.append(int(j))
        b.append(a)
    l = func(b)
    print(max(l) ** 2)