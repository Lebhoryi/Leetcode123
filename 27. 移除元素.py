# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    27. 移除元素.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/4/20 4:42 PM
'''
def removeElement(nums, val):
    if not nums:  return 0
    # for i in range(len(nums)-1, -1, -1):
    #     if nums[i] == val:
    #         nums.pop(i)
    # return len(nums)

    while val in nums:
        nums.remove(val)

    return len(nums)


nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums, val))
print("nums: {}".format(nums))