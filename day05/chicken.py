"""
求解《百钱百鸡》问题
1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
问公鸡 母鸡 小鸡各有多少只

Version: 0.1
Author: 子梁
Date: 2020-01-06
"""

import time

def exhaustion():
    time.perf_counter()
    t0=time.perf_counter()
    for x in range(0, 20):
        for y in range(0, 33):
            z = 100 - x - y
            if 5 * x + 3 * y + z / 3 == 100:
                 print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))
    t1=time.perf_counter()
    print("O(N^2) Time used:",t1 - t0)

def exhaustion_new():
    time.perf_counter()
    t0=time.perf_counter()
    for k in range(0,4):
        x = 4*k
        y = 25 - 7*k
        z = 75 + 3*k
        print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))
    t1=time.perf_counter()
    print("O(N) Time used:",t1 - t0)

def main():
    exhaustion()
    exhaustion_new()


if __name__ == '__main__':
    main()
