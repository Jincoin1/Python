#如何创建字典
#------------------dict={'key1':'value1','key2':'value2'}-------------------   
dictA={'name':1,'age':2,'school':3,'pop':4}#创建字典
print(dictA)
print(type(dictA))#查看类型
print(len(dictA))#查看长度
#----------------------字典的查询
print(dictA['name'])#查询a的值
#----------------------字典的修改-------------------------
dictA['name']='材质为'
dictA['age']='20'
dictA['school']='九江学院'
dictA['pop']='study'
print(dictA)
#-------------------------------------------------
dictA.update({'name':'才子为'})#----字典内容更新--利用.updata方法
print(dictA)
# #----------------------字典的key
# print(dictA.keys())#查看key
# print(dictA.values())#查看value
#----获取全部key（键）和value（值）
#第一种获取的方法
# for item in dictA.items():
#     print(item)  
# #第二种方法
# for key,value in dictA.items():
#     print('%s==%s'%(key,value))
    #==================================
#----------------------字典的删除-------------------------
del dictA['name']#删除name--通过指定键删除
print(dictA)
#利用.pop方法删除--通过指定键删除
dictA.pop('age')
print(dictA)
#如何排序，按照key排序
print(sorted(dictA.items(),key=lambda d:d[0]))#按照key排序-----要考虑字符类型不然会报错
#如何排序，按照value排序
print(sorted(dictA.items(),key=lambda d:d[1]))#按照value排序------要考虑字符类型不然会报错

