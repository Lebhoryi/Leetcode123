# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    28. 实现 strStr().py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/4/20 5:10 PM
'''
def strStr(haystack, needle):

    # 我想出来的
    # if not needle:  return 0
    # if not needle:  return -1
    # return haystack.index(needle) if needle in haystack else -1

    # 用内置函数
    # return haystack.find(needle)

    # 不用内置函数
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1



haystack = "hello"
needle = "ll"
print(strStr(haystack, needle))


