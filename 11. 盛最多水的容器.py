# coding=utf-8
"""
@ Summary: 双指针法
@ Update:  

@ file:    11. 盛最多水的容器.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-7-4 上午1:08
"""

def maxArea(height):
    if not height or len(height) < 2:  return 0

    # 暴力法，超时
    # maxarea = 0
    # for i in range(1, len(height)):
    #     for j in range(i):
    #         maxarea = max(min(height[i],height[j])*(i-j) , maxarea)
    # return maxarea

    # 双指针法
    maxarea, l, r = 0, 0, len(height)-1  # 最大面积，左边界， 右边界
    while l < r:
        maxarea = max(min(height[l], height[r])*(r-l), maxarea)
        if height[l] > height[r]:

            r -= 1
        else:
            l += 1
    return maxarea




height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))