#多继承
#子类额可以拥有多个父类，并且具有所有父类的属性和方法
class Father(object):
    def money(self):
        print("money")
class Mother(object):
    def apperance(self):
        print("beautiful")
    def money(self):
        print("mather's money")
class Son(Mother,Father): #子类
    pass
son = Son()
son.money()
son.apperance()