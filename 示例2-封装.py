#封装
#面向对象的三大特性：封装，继承，多态
#封装：指的是隐藏对象中一些不希望被外部所访问到的属性或者方法
# class Person:
#     name = "bbb"    #类属性
# pe = Person()
# print(pe.name)
# Person.name = "zizi"
# print(Person.name)

#隐藏属性（私有权限），只允许在类的内部使用，无法通过对象访问
#在属性名或则方法名前面加上两个下划线__
# class Person:
#     name = 'james' #类属性
#     __age = 28  #隐藏属性
#     def introduce(self):
#         print(f"{Person.name}的年龄是{Person.__age}") #在实例对象中访问隐藏属性
# pe = Person()
# print(pe.name)
# print(pe._Person__age)
# pe._Person__age = 18
# print(pe._Person__age)
# #第二种方法，在类的内部访问 ---推荐
# pe.introduce()

#私有属性/方法
#xxx:普通方法/属性，类中定义的可在任意地方使用
#_xxx:单下划线开头，声明私有属性/方法，如果定义在类中，外部可以使用，子类也可以继承
#      但是在另一个py文件中通过from xxx import * 导入时，无法导入
#__xxx:双下划线开头，隐藏属性，如定义在类中，无法在外部直接访问，子类不会继承，
#      要访问只能通过间接的方式，另一个py文件中通过from xxx import * 导入的时候 也无法导入
# 这种命名一般是python中的魔术方法或属性，都是有特殊含义或者功能的，直接不要轻易定义


class Person:
    name = "jjjj"
    __age = 22      #隐藏属性（双下划线
    _sex = "buanbunv"   #私有属性（单下滑线
pe = Person()
print(pe._sex)  #--->正确使用方式
#使用对象._类名__属性名访问隐藏属性
print(pe._Person__age)
#print(pe._Person_sex) #不能这样使用会报错-> #AttributeError: type object 'Person' has no attribute '_Person_sex'

class Man:
    def __play(self): #隐藏方法
        print("cjw")

    def _aaa(self):
        print("fangfa")

    def funa(self):     #实例方法
        print("pppp")
        Man.__play(self)    #在实例方法中调用隐藏方法
        Man._aaa(self)      #在实例方法中调用私有方法
       
        self.__play()#--->推荐使用
        self._aaa()#----->推荐使用
pe = Man()
pe.funa()