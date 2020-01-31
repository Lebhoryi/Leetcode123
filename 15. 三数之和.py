# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    15. 三数之和.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    1/31/20 10:35 PM
'''
def threeSums(nums):
    if not nums:  return []

    # # 暴力法，超时
    # nums.sort()
    # res = set()
    # for i in range(len(nums)-2):
    #     if i >= 1 and nums[i] == nums[i-1]:
    #         continue
    #     l = []
    #     for j in range(i+1, len(nums)):
    #         if nums[j] not in l:
    #             l.append(-(nums[i]+nums[j]))
    #         else:
    #             res.add((nums[i], nums[j], -(nums[i] + nums[j])))
    #
    # return list(map(list, res))

    nums.sort()
    res = []
    for i in range(len(nums)-2):
        # 去重
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            # print(res[i])
            if nums[i] + nums[l] + nums[r] == 0:
                res.append([nums[i], nums[l], nums[r]])
                # 去重 +1
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
            elif nums[i] + nums[l] + nums[r] < 0:
                l += 1
            else:
                r -= 1
    return res


nums = [-1,0,1,2,-1,-4]
print(threeSums(nums))