# coding=utf-8
'''
@ Summary: 如果要返回下标，先排序然后二分类找到这个值，最后用index()
@ Update:  

@ file:    81. 搜索旋转排序数组 II.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/26/20 10:56 PM
'''
def search(nums: [int], target: int) -> bool:
    return target in nums

if __name__ == "__main__":
    import sys
    nums = list(map(int, sys.stdin.readline().strip().split(",")))
    target = int(sys.stdin.readline())
    print(search(nums, target))