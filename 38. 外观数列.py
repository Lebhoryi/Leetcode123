# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    38. 外观数列.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/7/20 9:44 PM
'''
import re

def countAndSay(n: int) -> str:
    if n == 1: return "1"
    return re.sub(r'(.)\1*', lambda m: str(len(m.group())) + m.group(1), countAndSay(n - 1))

n = 4
print(countAndSay(n))