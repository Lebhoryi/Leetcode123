# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    18. 四数之和.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/2/20 3:00 PM
'''
import bisect

def fourSum(nums, target):
    if not nums or len(nums) < 4:  return []

    nums, res = sorted(nums), []   # 排序， 结果存储
    for i in range(len(nums)-3):  # 第一层遍历
        for j in range(i+1, len(nums)-2):  # 第二城遍历
            # 双指针法，左右指针
            r = len(nums) - 1
            # 二分查找， 节省时间
            l = max(j+1, bisect.bisect_left(nums, (target - nums[i] - nums[j] - nums[r]), j+1, len(nums)-1)-1)
            while l < r:
                f_sum = nums[i] + nums[j] + nums[l] + nums[r]
                if f_sum == target:
                    # 去重
                    if [nums[i], nums[j], nums[l], nums[r]] not in res:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif f_sum < target:
                    l += 1
                else:
                    r -= 1
    return res


nums = [-1,0,1,2,-1,-4]
target = -1
print(fourSum(nums, target))