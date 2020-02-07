# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    33. 搜索旋转排序数组.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/7/20 12:22 AM
'''
def search(nums: [int], target: int) -> int:
    l, r, res = 0, len(nums)-1, -1
    if not nums:  return res
    while l < r-1:
        mid = (l + r) // 2
        if nums[l] < nums[mid]:  # mid左边是个顺序数组
            if nums[l] <= target and nums[mid] >= target:
                r = mid
            else:
                l = mid
        else:  # mid 右边是个顺序数组
            if nums[r] >= target and nums[mid] <= target:
                l = mid
            else:
                r = mid

    if nums[l] == target:
        res = l
    elif nums[r] == target:
        res = r
    return res


nums = [5, 1, 3]
target = 5
print(search(nums, target))