# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    66. 加一.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/22/20 11:06 PM
'''

def plusOne(digits: [int]) -> [int]:
    # y = list(map(int, str(x))); x = 123; y = [1, 2, 3]
    return list(map(int, str(int("".join(map(str, digits))) + 1)))

digits = [1, 2, 3]
print(plusOne(digits))