# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    13. 罗马数字转整数.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    1/30/20 10:14 PM
'''
def romantoInt(s):
    d = {"I": 1, "IV": 3, "V": 5, "IX": 8, "X": 10, "XL": 30, "L": 50, "XC": 80, "C": 100, "CD": 300, "D": 500,
         "CM": 800, "M": 1000}

    for i in range(len(s)):
        if i == 0:
            res = d[s[i]]
        elif s[i-1:i+1] in d:
            res += d[s[i-1:i+1]]
        else:
            res += d[s[i]]

    return res

s = "III"
print(romantoInt(s))
