"""
找出所有的水仙花数(超完全数字不变数、自恋数、自幂数、阿姆斯特朗数)
三位数，每个数字的立方数之和正好等于他本身

Version: 0.1
Author: 子梁
Date: 2020-01-06

"""

for num in range(100,1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)