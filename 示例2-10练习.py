#coding: utf-8
'''
import os

fp=open('noto.txt','w')#打开文件 w--->write
print('beibeiebi',flie=fp)# 将biebeibei写入文件
fp.close()#关闭文件

os.remove('noto.txt')#删除文件

num=input('%d')
print('数字%d'+num)
num=int(num)
print('数字%d',num)

name=input('请输入你的名字：')
age=input('请输入你的年龄：')
motto=input('请输入你的座右铭：')
print('--------自我介绍--------')
print('你的名字是：%s'%name)
print('你的年龄是：%s'%age)
print('你的座右铭是：%s'%motto)

a=20
b=30
print(a==b)
print(a>=b)
print(a<=b)
print(a!=b)
print(a>b)
print(a<b)

a=20
b=30
c=40
d=50
print(a+b>c and c+d>a)#and 必须两个真 真True  Flase错
print(a+b>c or c+d>a)#or 一个真就真   
print(not a+b>c)#取反 真假交换，真的变成假的
#优先级
#---->not>and>or

------------------------------------
'''
name=input('请输入你的名字：')
age=input('请输入你的年龄：')   
motto=input('请输入你的座右铭：')   
print('--------自我介绍--------')
print("名字{}，年龄{}，座右铭{}".format(name,age,motto))#format格式化输出
print('---------------#format格式化输出---------')