# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    43. 字符串相乘.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/15/20 7:52 PM
'''
def multiply(num1: str, num2: str) -> str:
    d, res = {}, 0
    for i, n1 in enumerate(num1[::-1]):
        for j, n2 in enumerate(num2[::-1]):
            d[i+j] = d.get(i+j, 0) + int(n1)*int(n2)
    for i, value in d.items():
        res += value * (10**i)

    return str(res) or "0"

num1 = "245"
num2 = "42"
print(multiply(num1, num2))