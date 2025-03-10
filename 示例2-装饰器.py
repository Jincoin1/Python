def outer(fun):
    def inner(name):
        print(f"{name}是inner函数中的参数")
        print("haha")
        fun(name)
    return inner
@outer#---相当于执行了 funr = outer(funr)
def funr(name):
    print("这是被装饰的函数")
funr("bibibi")