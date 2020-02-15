# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    46. 全排列.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/15/20 9:20 PM
'''
def permute(nums: [int]) -> [[int]]:
    # 方法一： 内置函数
    # from itertools import permutations
    # return list(permutations(nums))

    # 方法二： 回溯法
    res, path, nums = [], [], sorted(nums)
    def dfs(nums, path):
        if not nums:
            res.append(path[:])
        for i in range(len(nums)):
            dfs(nums[:i]+nums[i+1:], path+[nums[i]])
    dfs(nums, path)
    return res


    # 高手版本
    # return [[n] + sub for i, n in enumerate(nums) for sub in permute(nums[:i]+nums[i+1:])] or [[]]


nums = [1, 2, 3]
print(permute(nums))
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
