# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    26. 删除排序数组中的重复项.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/3/20 11:09 PM
'''
def removeDuplicates(nums):
    # for i in range(len(nums)-1, 0, -1):
    #     if nums[i] == nums[i-1]:  nums.pop(i)
    # return len(nums)
    i = 0
    for j in range(i+1, len(nums)):
        if nums[i] != nums[j]:
            nums[i+1] = nums[j]
            i += 1
    return i+1

nums = [0,0,1,1,1]
print(removeDuplicates(nums))
print(nums)