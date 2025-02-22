'''
strMage="hEllo"
strMage1="     world         "
print(strMage[1])#打印第二个字符
print(strMage.lower())#打印小写
print(strMage.upper())#打印大写
print(strMage.startswith("h"))#判断是否以h开头,正确返回True
print(strMage.endswith("o"))#判断是否以o结尾，正确返回True
print(strMage.find("l"))#查找l的位置，成功返回下标，失败返回-1
print(strMage.index("l"))#查找l的位置，成功返回下标，失败抛出异常
print(id(strMage))#返回字符串的id-->地址
print(strMage1.lstrip())#去掉左边的空格
print(strMage1.rstrip())#去掉右边的空格


'''
strMage="hEllo world"
#slice=[star:stop:step]----start:开始位置，stop:结束位置，step:步长
# start<=x<stop
print(strMage[0:5])#打印从0到5的字符
print(strMage[0:5:2])#打印从0到5的字符，步长为2
print(strMage[::-1])#反向打印
print(strMage[2:])#第三个字符到最后
print(strMage[:5])#前五个字符
print(strMage[:])#全部打印
print(strMage[-1])#打印最后一个字符