# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    88. 合并两个有序数组.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/27/20 11:34 PM
'''
def merge(nums1: [int], m: int, nums2: [int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # nums1[m:] = nums2
    # nums1.sort()

    while n > 0:
        if m and nums1[m-1] > nums2[n-1]:
            nums1[n+m-1], m = nums1[m-1], m-1
        else:
            nums1[n+m-1], n = nums2[n-1], n-1


nums1 = [1,2,3,0,0,0]; m = 3
nums2 = [2,5,6];       n = 3
merge(nums1, m, nums2, n)
print(nums1)