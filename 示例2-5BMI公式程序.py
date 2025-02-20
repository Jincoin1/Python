# BMI公式:體重(公斤)/身高(公尺)平方
print('BMI公式:體重(公斤)/身高(公尺)平方')
height=input('請輸入身高(M):')
weight=input('請輸入體重(KG):')
BMI=float(weight)/float(height)**2
print('BMI為:',BMI)
if BMI<18.5:
    print('體重過輕')
elif 18.5<=BMI<25:
    print('正常範圍')
elif 25<=BMI<28:
    print('過重')
elif 28<=BMI<32:
    print('輕度肥胖')   
elif BMI>=32:
    print('肥胖')
