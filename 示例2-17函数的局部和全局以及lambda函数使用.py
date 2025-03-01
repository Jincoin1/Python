# a = 10  #全局变量
# def test1():
#     global a    #global使得全局变量可修改
#     a = 300 #局部变量优先使用
#     print("test1----a=%d:"%a)
#     a = 200 
#     print("test1----a=%d:"%a)

# def test2():

#     print("test2-----a=%d:"%a)#没有局部变量，使用全局变量

# test1()
# test2()

reslut=lambda a,b,c:a+b+c
print(reslut(1,2,3))
#lambda与三元运算
reslut1=(lambda x,d,t:x if x>d else t)#三元操作，简化代码，缺点是只可以用一个表达式
print(reslut1(2,1,3))
age = 14
print("可进去" if age >= 18 else "未成年不得进入")