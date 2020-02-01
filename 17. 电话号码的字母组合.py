# coding=utf-8
'''
@ Summary: 笛卡尔积
@ Update:  

@ file:    17. 电话号码的字母组合.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/1/20 10:44 PM
'''
from itertools import product

def letterCombinations(digits):
    l = "- - abc def ghi jkl mno pqrs tuv wxyz".split()
    return ["".join(j) for j in product(*[l[int(i)] for i in digits])] if digits else []



digits = "23"
print(letterCombinations(digits))