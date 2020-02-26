# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    80. 删除排序数组中的重复项 II.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/26/20 10:06 PM
'''
def removeDuplicates(nums: [int]) -> int:
    for i in range(len(nums)-3, -1, -1):
        if nums[i] == nums[i+1] and nums[i] == nums[i+2]:
            nums.pop(i)
    return len(nums)

if __name__ == "__main__":
    import sys
    nums = list(map(int, sys.stdin.readline().strip().split(",")))

    print(removeDuplicates(nums))
    print(nums)