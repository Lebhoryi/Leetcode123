# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    35. 搜索插入位置.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/7/20 7:48 PM
'''

def searchInsert(nums: [int], target: int) -> int:
    # import bisect
    return bisect.bisect_left(nums, target)