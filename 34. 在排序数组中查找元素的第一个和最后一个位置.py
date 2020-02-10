# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    34. 在排序数组中查找元素的第一个和最后一个位置.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/7/20 7:59 PM
'''
import bisect
def searchRange(nums: [int], target: int) -> [int]:
    if not nums or target not in nums:  return [-1, -1]
    l, r = bisect.bisect_left(nums, target), bisect.bisect_right(nums, target)-1
    return [l, r]

nums = [5,7,7,8,8,10]
target = 7
print(searchRange(nums, target))