"""
格式化输出

Version: 0.1
Author: 子梁
Date: 2019-12-10
"""
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b)) # 整形
print('%d - %d = %d' % (a, b, a - b)) # 整形
print('%d * %d = %d' % (a, b, a * b)) # 整形
print('%d / %d = %f' % (a, b, a / b)) # 整形、浮点
print('%d // %d = %d' % (a, b, a // b)) # 整形
print('%d %% %d = %d' % (a, b, a % b))  # 整形
print('%d ** %d = %d' % (a, b, a ** b)) # 整形