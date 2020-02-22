# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    67. 二进制求和.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/22/20 11:27 PM
'''

def addBinary(a: str, b: str) -> str:
    # 二进制 to 十进制 to 二进制
    return bin(int(a, 2) + int(b, 2))[2:]

a = "11"
b = "1"
print(addBinary(a, b))