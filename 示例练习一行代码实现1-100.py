#coding: utf-8
if __name__ == "__main__":
    total = 0
    total2 = 0
    for i in range(101):
        total += i
    print('total:',total)

    for a in range(101):
            total2 += a
    print('total2:', total2)
            
    for c in range (3):
            print(c)

----------------------------
----------------------------
'''
# 禁用默认分隔符
print('G','F','G', sep='')
# 使用-作为分隔符
print('8','6','2019', sep='-')
# 另一个定制分隔符例子
print('logan','芒果文档', sep='@')

--------------------------------------------

print('G','F', sep='', end='')
print('G')
#\n 会在打印后换行
print('9','12', sep='-', end='-2016\n')
print('prtk','agarwal', sep='', end='@')
print('芒果文档')

======================

#输出结果

GFG
8-6-2019
logan@芒果文档
--------------------
GFG
9-12-2016
prtkagarwal@芒果文档

'''
