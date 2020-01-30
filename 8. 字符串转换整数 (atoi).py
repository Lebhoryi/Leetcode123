# coding=utf-8
'''
@ Summary: 我佛了，试了两个小时的各种加条件限制，正则一行搞定
@ Update:  

@ file:    8. 字符串转换整数 (atoi).py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    1/30/20 3:36 PM
'''
import re

def myAtoi(s):
    return max(min(int(*re.findall("^[\+\-]?\d+", s.lstrip())), 2**31-1), -2**31)
    # return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2 ** 31 - 1), -2 ** 31)


# print([str(i) for i in range(10)])
l_str = ["-5-", "-abc", "2147483648", "+-2", "+1", "42", "   -42", "4193 with words", "words and 987", "-91283472332"]
for item in l_str:
    # print(item[0])
    print(myAtoi(item))