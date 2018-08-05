def HeapSort(heap):#将根节点取出与最后一位做对调，对前面len-1个节点继续进行对调整过程。
    Build_MAX_Heap(heap)
    for i in range(len(heap)-1,-1,-1):
        #当前最顶的数（最大数）往后放，递归
        heap[0],heap[i] = heap[i],heap[0]
        MAX_Heapify(heap, i, 0)
    return heap

def Build_MAX_Heap(heap):#构造一个堆，将堆中所有数据重新排序
    HeapSize = len(heap)#将堆的长度当独拿出来方便
    for i in range((HeapSize -2)//2,-1,-1):#从后往前出数
        #所有有子节点的节点个数：HeapSize -2)//2
        MAX_Heapify(heap,HeapSize,i)

def MAX_Heapify(heap,HeapSize,root):#在堆中做结构调整使得父节点的值大于子节点
    #通常堆是通过一维数组来实现的。在阵列起始位置为0的情况中
    #(1)父节点i的左子节点在位置(2 * i + 1);
    #(2)父节点i的右子节点在位置(2 * i + 2);
    left = 2*root + 1
    right = left + 1
    larger = root
    if left < HeapSize and heap[larger] < heap[left]:
        larger = left
    if right < HeapSize and heap[larger] < heap[right]:
        larger = right
    if larger != root:#如果做了堆调整则larger的值等于左节点或者右节点的，这个时候做对调值操作
        heap[larger],heap[root] = heap[root],heap[larger]
        #将最大的数放最顶，对底下可能有的子树继续调整
        MAX_Heapify(heap, HeapSize, larger)



a = [30,50,57,77,62,78,94,80,84]
print(a)
HeapSort(a)
print(a)