#继承
#继承是让类和类之间转变为父子关系，子类默认继承父类的属性和方法
#1.1语法
#class类名（父类名）
#  代码块
#1.2单继承
# class Person():
#     def eat(self):
#         print("我会唱歌")
#     def sing(self):
#         print("我是唱歌小能手")
# class Girl(Person): #Person类的子类
#     pass #占位符，代码里面类下面不写任何对象，会自动跳过
# class Boy(Person): #Person类的子类
#     pass
# girl = Girl()
# girl.eat()
# girl.sing()
# print("")
# boy = Boy()
# boy.eat()
#boy.sing()
#总结：子类可以继承父类的属性和方法，就算子类总结没有，也可以使用父类的
#1.3继承的传递（多重继承）
#A/B/C C(子类)继承与B(子类)继承A类(父类)，C类具有A/B的属性和方法
#子类拥有父类的父类属性和方法
# class Father():
#     def eat(self):
#         print("cf")
#     def sleep(self):
#         print("sj")
# class Son(Father):  #Father类的子类
#     pass
# class Grandson(Son):
#     pass
# son = Son()
# son.eat()
# grandson = Grandson()
#grandson.eat()
#继承的传递性就是子类拥有父类的以及父类中的属性方法
#==============================
#重写指在子类中定义与父类相同名称的方法
#覆盖的方法
# class Person:
#     def money(self):
#         print("yibaiwan jicheng")
# class Man(Person): #子类
#     def money(self):
#         print("自己赚钱")#子类有一样的优先用子类的，覆盖效果。
# man = Man()
# man.money()
#对父类方法进行扩展：继承父类的方法，子类也可以增加自己的功能
#父类名.方法名（self)
#super().方法名() -----推荐使用
#super()在python里面是一个特殊的类，super（）是使用super类创建出来的对象，可以调用父类中的方法
#supper (子类名,self).方法名()
# class Person:
#     def money(self):
#         print("yibaiwan jicheng")
#     def sleep(self):
#         print("ssssjjjj")
# class Man(Person): #子类
#     def money(self):
#         Person.money(self)  # 方法一
#         super().money()
#         super().sleep()
#         super(Man,self).money()
#         print("自己赚钱")
# man = Man()
# man.money()
print(dir(object))