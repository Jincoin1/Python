'''
for data in range(1,200):
    if data%2==0:
        print("%d偶数"%data)
        pass
    else:
        print("%d奇数"%data)
        pass
print(-------for的使用-------)

sum=0
for data in range(1,101):
    if sum>=100:
        print("循环到data是%d时结束循环"%data)
        break
    sum+=data
print("1-100的和是%d"%sum)


print('--------break和continue的使用---------')
for iteam in 'i  love python':
    if iteam=='o':
        continue
    print(iteam,end='')
    pass

for iteam in 'i  love python':
    if iteam=='p':
        break
    print(iteam,end='')
    pass

print('--------for实现99乘法表---------')
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%-4d"%(i,j,i*j),end='')
        pass
    print()
    pass

------------for-else的使用-----------
account='www'
pwd='123'
for i in range(3):
    account=input("请输入账号：")
    pwd=input("请输入密码：")
    if account=="www" and pwd=="123":
        print("登陆成功")
        break
    pass
else :
    print("账号密码错误，登陆失败")
    pass
'''
index=1
while index<=10:
    print(index)
    if index==6:
        print("index等于6时跳出循环")
        break
    index+=1
    pass
else:
    print("while循环正常结束")
    pass