# coding=utf-8
'''
@ Summary: 斐波那契数列
@ Update:  

@ file:    斐波那契数列.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    6/29/19 6:50 PM
'''

############
#1. 递归   #
############

# 消耗内存大
def fib1(n):
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)


############
#2. 循环   #
############

def fib2(n):
    res = [0, 1]
    while len(res) <= n:
        res.append(res[-1] + res[-2])
    return res[-1]

############
#3. 生成器 #
############

def fib3(n):
    a, b = 0, 1
    for i in range(n):
        yield b
        a, b = b, a + b

if __name__ == "__main__":
    print(fib1(10))
    print("###################")
    print(fib2(10))
    print("###################")
    print([n for n in fib3(10)][-1])
    print("###################")


