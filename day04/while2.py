"""
用while循环实现1~100之间的偶数求和

Version: 0.1
Author: 子梁
Date: 2020-01-06
"""

sum, num = 0, 2
while num <= 100:
    sum += num
    num +=2
print(sum)