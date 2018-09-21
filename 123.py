def fun1(fun):
    print('fun1 action')
    def func(*args,**kwargs):
        print(args)
        print(kwargs)
        print('fun3 action')
    return func
    #这也可以看出装饰器的一个作用，直接调用fun2是会报错的，可是这个程序现在能跑

@fun1
def fun2(a,b,c,d,e):
    print('fun2 action',e,d)


if __name__ == '__main__':
    fun2(1,2,3)
