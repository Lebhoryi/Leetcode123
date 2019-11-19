# coding=utf-8
"""
@ Summary: 
@ Update:  

@ file:    8.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-7-4 上午1:08
"""


def lengthOfLongestSubstring(s):
    # 滑动窗口
    left = 0
    max_len = 0  # 最长子串长度
    cur_len = 0  # 现有子串长度
    cur = set()  # 滑动的窗口
    for i in range(len(s)):
        cur_len += 1
        while s[i] in cur:
            cur.remove(s[left])
            left += 1
            cur_len -= 1
        cur.add(s[i])
        if max_len < cur_len:
            max_len = cur_len
    return max_len

a = "abcabcbb"
print(lengthOfLongestSubstring(a))