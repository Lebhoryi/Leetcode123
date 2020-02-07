# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    31. 下一个排列.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/5/20 9:53 PM
'''
def nextPermutation(nums: [int]):
    if nums[::-1] == sorted(nums):
        nums.sort()
    else:
        for i in range(len(nums)-1, 0, -1):
            # 从后往前看，如果倒数第一个数大于倒数第二个数，只需要交换最后两个数即可
            if i == len(nums)-1 and nums[i] > nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                break
            # 如果存在其他后一个数大于前一个数的，存在比nums 大的数
            # nums[i-1] 与 比nums[i-1]大一点的数字进行交换，并且对nums[i:]排序
            elif nums[i] > nums[i-1]:
                # for j in range(len(nums[i:])):
                #     nums[j] - nums[i-1]
                min_index = nums.index(min(nums[i:], key=lambda x:(x-nums[i-1])
                            if (x-nums[i-1]) > 0 else float('inf')), i,)
                nums[i-1], nums[min_index] = nums[min_index], nums[i-1]
                nums[i:] = sorted(nums[i:])
                break


nums = [5,4,7,5,3,2]
nextPermutation(nums)
print("nums: {}".format(nums))





