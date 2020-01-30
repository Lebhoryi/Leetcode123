# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    7. 整数反转.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    1/30/20 3:01 PM
'''
def reverse(x):
    x = int(str(x)[::-1] if x > 0 else str(x)[0] + str(x)[:0:-1])
    return x if x < 2**31-1 and x > -2**31 else 0

x = [123, -123, 120, 1534236469]
print(reverse(x[3]))
print(9646324351 > 2 ** 31 - 1)