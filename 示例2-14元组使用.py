#元组的创建不可修改
tupleA=()#创建空元组
tupleA=('abcd',89,9.12,'peter',[1,2,3,4,5])#创建元组
print(tupleA)
print(type(tupleA))#查看类型
print(tupleA[0])#打印第一个元素
#元组的查询
for item in tupleA:
    print(item,end=' ')
#print(tupleA[4][0])#打印第五个元素的第一个元素----打印list里的元素
#-----------------tupleA(str:end:step)-----------------
#print(tupleA[::-1])#倒序打印
#-----可以和list一样通过相同的方法打印元组里的元素
#print(tupleA[::-2])#表示反转字符串，每隔两个取一次
#print（tupleA[：：-3]）#表示反转字符串，每隔三个取一次
#print(tupleA[-2:-1]:)#表示反转字符串，取倒数第二个元素
#---------------------元组的修改
#tupleA[0]='peter'#元组不可修改,会报错。
tupleA[4][0]=200#元组里的list可以修改
print(tupleA)
#---------------------元组的删除
#------del tupleA[0]#元组不可删除，会报错。
tupleB=(1)
print(type(tupleB))#查看类型---<class 'int'>---显示是int类型
tupleC=(1,)
print(type(tupleC))#查看类型---<class 'tuple'>---显示是元组类型
#=========所以创建元组时，（）里面只有一个元素时，后面要加上逗号，不然会被认为是int类型==========================
#----------------------元组的运算
tupleD=tuple(range(10))
print(tupleD.count(1))#统计1出现的次数