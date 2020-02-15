# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    47. 全排列 II.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/15/20 10:33 PM
'''


def permuteUnique(nums: [int]) -> [[int]]:
    res, tmp, nums = [], [], sorted(nums)

    def dfs(nums, tmp):
        # 终止条件
        if nums == []:
            res.append(tmp[:])

        # 迭代
        for i in range(len(nums)):
            # 去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            dfs(nums[:i] + nums[i + 1:], tmp + [nums[i]])

    dfs(nums, tmp)
    return res

nums = [1, 1, 2]
print(permuteUnique(nums))