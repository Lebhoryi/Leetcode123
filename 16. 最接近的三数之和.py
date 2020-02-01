# coding=utf-8
'''
@ Summary: 想到了双指针法
@ Update:  

@ file:    16. 最接近的三数之和.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/1/20 2:27 PM
'''
import bisect

def threeSumClosest(nums, target):
    if not nums or len(nums) < 4:  return []

    nums, res = sorted(nums), float("inf")  # 排序，res:结果储存
    for i in range(len(nums)-2):
        # # 去重
        # if i > 2 and nums[i] == nums[i-1]:
        #     continue
        # 左指针， 右指针
        # 这个二分法很骚， 直接节省了一半的时间
        l = max(i+1, bisect.bisect_left(nums, target-nums[i]-nums[len(nums)-1], i+1, len(nums)-1)-1)
        r =  len(nums) - 1
        while res != target and l < r:
            sumThree = nums[i] + nums[l] + nums[r]
            # if abs(res-target) > abs(sumThree-target):
            #     res = sumThree
            # 下面一行与上面两行效果等同
            res = min(res, sumThree, key=lambda x: abs(x-target))
            # 移动左右指针
            l += (sumThree < target)
            r -= (sumThree > target)
    return res


nums = [-1, 2, 1, -4]
target = 1
print(threeSumClosest(nums, target))