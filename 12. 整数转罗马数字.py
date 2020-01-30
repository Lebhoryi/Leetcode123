# coding=utf-8
"""
@ Summary: 
@ Update:  

@ file:    12. 整数转罗马数字.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    1/30/20 10:04 PM
"""
def inttoRoman(num):
    if not num:  return num

    d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
    	100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X',
    	9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

    res = ""
    for key in d:
        if num // key != 0:
            count = num // key  # 罗马数字的个数
            res += count*d[key]  # 开始拼接罗马数字
            num %= key
    return res


num = [3, 4, 9, 18, 1994]
for item in num:
    print(inttoRoman(item))