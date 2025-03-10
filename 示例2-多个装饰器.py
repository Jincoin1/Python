def deco1(fun):
    def inner():
        return "学习python"+fun()+"晚上敲代码"
    return inner
#第二个装饰器
def deco2(fun):
    def inner():
        return "王余玄"+fun()+"才思维"
    return inner
@deco1
@deco2
def test1():
    return "晚上在学习python基础"
print(test1())
#学习python---王余玄晚上在学习python基础才思维---晚上敲代码
#多个函数装饰器的装饰过程，离函数最近的装饰先装饰，然后外面的装饰器再进行装饰，由内到外的装饰过程
    