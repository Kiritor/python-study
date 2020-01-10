"""
回文数

Version: 0.1
Author: 子梁
Date: 2020-01-06
"""

num = int(input('请输入一个正整数: '))
temp = num
num2 = 0
while temp > 0:
    num2 *= 10
    num2 += temp % 10
    temp //= 10
if num == num2:
    print('%d是回文数' % num)
else:
    print('%d不是回文数' % num)