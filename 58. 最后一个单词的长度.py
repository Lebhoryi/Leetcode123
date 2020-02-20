# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    58. 最后一个单词的长度.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/19/20 10:20 PM
'''

def lengthOfLastWord(s: str) -> int:
    return len(s.strip().split(" ")[-1])


s = " "
print(lengthOfLastWord(s))