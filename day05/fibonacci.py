"""
斐波拉契数列

Version: 0.1
Author: 子梁
Date: 2020-01-07
"""

a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end = ' ')
print('')