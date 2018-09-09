'''
输入一个单向链表，输出该链表中倒数第k个结点，链表的倒数第1个结点为链表的尾指针。

链表结点定义如下：
struct ListNode
{
      int m_nKey;
      ListNode* m_pNext;
};

详细描述：
接口说明
原型：
ListNode* FindKthToTail(ListNode* pListHead, unsignedint k);

输入参数：
ListNode* pListHead  单向链表
unsigned int k  倒数第k个结点

输出参数（指针指向的内存区域保证有效）：
无

返回值：
正常返回倒数第k个结点指针，异常返回空指针

输入
8
1 2 3 4 5 6 7 8
4

输出
5
'''

while True:
    try:
        n = int(input())
        s = input().split()
        k = int(input())
        if k == 0:
            print(0)
        else:
            print(s[-k])
    except:
        break
#在这个OJ上，Python用列表写更容易
#split注意用默认就行
#记得是if else，不要漏了else