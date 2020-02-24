# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    75. 颜色分类.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/25/20 12:19 AM
'''


def sortColors(nums: [int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # 简单版快排，使用了额外的空间，不符合题意，做升级版
    # if not nums or len(nums) < 2: return nums
    # pivot_index = 0
    # pivot = nums[pivot_index]
    # left = [i for i in nums[pivot_index+1:] if i <= pivot]
    # right = [i for i in nums[pivot_index+1:] if i > pivot]
    # return sortColors(left) + [pivot] + sortColors(right)


    # 升级版，原地快排
    l, cur, r = 0, 0, len(nums) - 1
    while l <= r:
        if nums[l] == 0:  # 当左指针为0，把先前的1换掉
            nums[l], nums[cur] = nums[cur], nums[l]
            cur += 1
            l += 1
        elif nums[l] == 2:  # 当左指针为2时，放到最右边去，然后右指针往左走
            nums[l], nums[r] = nums[r], nums[l]
            r -= 1
        else:
            l += 1


nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums)