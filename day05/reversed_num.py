"""
正整数反转

Version: 0.1
Author: 子梁
Date: 2020-01-06

"""

num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)