# li=[]
# print(type(li))#查看类型
# lisA=['ababab','fffff','ccccc',4,5,6,7,8,9]#创建列表    
# print(lisA[0])#打印列表一个元素
# lisA.append('aaaaa')#添加元素
# print(lisA)

# lisA.insert(0,'00000')#在第一个元素后面插入元素

# rsData=list(range(10))#创建一个0-9的列表
# print(rsData)#打印列表
# print(type(rsData))#查看类型
# lisA.extend(rsData)#将rsData的元素添加到lisA中
# print(lisA)#打印新列表

# #print(-----------------------修改-----------------------)
# print('修改前',lisA)
# lisA[0]='peter'
# print('修改后',lisA)


#print(---------------------删除list数据项-------------------------------------)
listB=list(range(10,30))
print('删除前',listB)
del listB[0]#删除第一个元素
del listB[1:3]#删除第二个到第四个元素
print('删除后',listB)
listB.remove(11)#删除第一个11
print('删除后',listB)
listB.pop(1)#移除制定的项，参数是索引值--下标
print('删除后',listB)

print(listB.index(19))#查找19的位置

print(listB.index(19,8,10))#查找19的位置，范围是0-10--（下标）
