def merge(list):
    if len(list) <= 1:
        return list
    mid = len(list)//2
    list1 = merge(list[:mid])
    list2 = merge(list[mid:])
    return mergeSort(list1,list2)

def mergeSort(list1,list2):
    ans = []
    a=0
    b=0
    while a<len(list1) and b<len(list2):
        if list1[a] <= list2[b]:
            ans.append(list1[a])
            a += 1
        else:
            ans.append(list2[b])
            b += 1
    while a<len(list1):
        ans.append(list1[a])
        a += 1
    while b<len(list2):
        ans.append(list2[b])
        b += 1
    return ans

arr = [2,3,1,3,4,1,2,3]
a = merge(arr)
print(arr)
print(a)