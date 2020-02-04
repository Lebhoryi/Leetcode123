# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    29. 两数相除.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/4/20 10:24 PM
'''
def divide(dividend: int, divisor: int):
    a, b, ret, t = abs(dividend), abs(divisor), 0, 1
    while a >= b:
        if a >=b:
            ret += t
            a -= b
            b += b
            t += t
        else:
            t >>= 1
            b >>= 1
    ret = ret if dividend ^ divisor >= 0 else -ret
    return min(max(ret, -2**31), 2**31-1)



dividend = 10
divisor = 3
print(divide(dividend, divisor))