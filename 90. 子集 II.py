# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    90. 子集 II.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    3/1/20 9:40 PM
'''
from itertools import combinations

def subsetsWithDup(nums: [int]) -> [[int]]:
    res, path, n, nums = [], [], len(nums), sorted(nums)
    def dfs(nums, path):
        # 终止条件
        if len(path) <= n:
            res.append(path[:])

        for i in range(len(nums)):
            # 剪枝，去重
            if i != 0 and nums[i] == nums[i-1]:
                continue
            dfs(nums[i+1:], path + [nums[i]])

    dfs(nums, path)
    return res

if __name__ == "__main__":
    import sys

    nums = list(map(int, sys.stdin.readline().strip()[1:-1].split(",")))
    print(subsetsWithDup(nums))
