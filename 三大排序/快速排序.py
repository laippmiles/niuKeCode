def quick(arr,firstIndex,lastIndex):
    if firstIndex >= lastIndex:
        return
    divIndex = getdivIndex(arr,firstIndex,lastIndex)
    quick(arr,firstIndex,divIndex)
    quick(arr,divIndex+1,lastIndex)

def getdivIndex(arr,firstIndex,lastIndex):
    i = firstIndex -1
    for j in range(firstIndex,lastIndex):
        if arr[j] <= arr[lastIndex]:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[lastIndex] = arr[lastIndex],arr[i+1]
    return i

a = [2,3,4,1,2,5,6]
print(a)
quick(a,0,len(a)-1)
print(a)