# coding=utf-8
'''
@ Summary: DP
@ Update:  

@ file:    53. 最大子序和.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/17/20 9:09 PM
'''
def maxSubArray(nums: [int]) -> int:
    for i in range(1, len(nums)):
        nums[i] = max(nums[i], nums[i] + nums[i-1])
    return max(nums)

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))