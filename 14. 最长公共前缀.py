# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    14. 最长公共前缀.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    1/31/20 2:27 PM
'''
import os

def longestCommonPrefix(strs):
    # return os.path.commonprefix(strs)

    # 利用zip和set
    # + [0] 是为了防止出现 ["a", "a"]的情况
    l = [len(set(i)) == 1 for i in zip(*strs)] + [0]
    return strs[0][:l.index(0)] if strs else ""

strs = [["aa","aa"], ["c","c"], ["",""], ["flower","flow","flight"], ["dog","racecar","car"]]
[print(longestCommonPrefix(item)) for item in strs]