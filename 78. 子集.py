# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    78. 子集.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/25/20 11:35 PM
'''
def subsets(nums: [int]) -> [[int]]:
    from itertools import combinations
    res = []
    for i in range(len(nums)+1):
        res += list(map(list, combinations(nums, i)))
    return res

nums = [1,2,3]
print(subsets(nums))