import random
person=int(input('请输入你要出的拳头：1.石头 2.剪刀 3.布'))
computer=random.randint(1,3)#生成随机数
if person==1 and computer==2 :
    print('你赢了')
elif person==2 and computer==3:
    print('你赢了')
elif person==3 and computer==1:
    print('你赢了')
elif person==computer:
    print('平局')
else:
    print('你输了')

    if computer==1:
        computer='石头'
    elif computer==2:
        computer='剪刀'  
    else:
        computer ='布'
    print('电脑出的是：'%computer)