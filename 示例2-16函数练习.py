#-----------------函数实现数据相加，任意输入n个数字，返回这些数字的和。
#map(int, ...): 将输入的字符串转换为整数
#例如，['1', '2', '3', '4', '5'] 会被转换为 [1, 2, 3, 4, 5]
#.split(): 将输入的字符串按空格分割
#例如，'1 2 3 4 5' 会被分割成 ['1', '2', '3', '4', '5']
# tuple(...):
# 将 map 函数返回的迭代器转换为一个元组。
# 例如，[1, 2, 3, 4, 5] 会被转换为 (1, 2, 3, 4, 5)。
# def receive(data_tuple):
#     return sum(data_tuple)

# Tuple=tuple(map(int,input("输入数据，用空格分隔：").split()))
# print('求得的Sum值为:',receive(Tuple))
#================================================================================================
#-----------------------随机输入一串数据，返回其中的奇数
#方法与上面类似，只是在returnlist函数中加入了判断条件
# def returnlist(args):
#     list1 = []
#     for i in args:
#         if i%2==1:
#             list1.append(i)
#     return  list1 

# Number=list(map(int,input("输入数据，用空格分隔：").split()))
# print('生成了新的列表:',returnlist(Number))
#================================================================================================
def returnlen(dictionary):
	new_Dict={}
	for key,value in dictionary.items():
		value_str= str(value)
		if len(value) > 2:
			new_Dict[key]=value_str[:2]
		else :  
			new_Dict[key]=value_str
	return new_Dict

dictA={'name':'123','age':'123','school':'12','pop':'1234'}
receive=returnlen(dictA)
print(receive)
