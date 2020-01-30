# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    9.回文数.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    1/30/20 6:11 PM
'''
def isPalindrome(x):
    return str(x) == str(x)[::-1]

x = 101
print(isPalindrome(x))