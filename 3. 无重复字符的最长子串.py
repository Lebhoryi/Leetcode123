# coding=utf-8
'''
@ Summary: 窗口滑动
@ Update:  

@ file:    3. 无重复字符的最长子串.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    1/28/20 4:00 PM
'''
def lenthOfLongestSubstring(s):
    if not s:  return s

    left, max_lenth = 0, 1  # 左边界， 最大长度
    lenth = len(s)  # 字符串长度
    for right in range(lenth):
        # 当右边界的值在之前的子串中出现时，左边界移动排除
        while s[right] in s[left:right]:
            left += 1
        # 记录最长子串长度
        if max_lenth < (right-left+1):
            max_lenth = right-left+1
    return max_lenth



s = "abcabcbb"
# s = "pwwkew"
# s = "dvdf"
print(lenthOfLongestSubstring(s))