'''
求和

Date:2019/02/25
'''

class Solution(object):
    '''求和
    
    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
    

    '''
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
        
    def twoSum(self):
        for i in range(len(self.nums)-1):
            for j in range(i+1, len(self.nums)):
                if self.nums[i] + self.nums[j] == self.target:
                    return i, j

nums = [2, 7, 11, 15]
target = 9

solu = Solution(nums, target)
print(solu.twoSum())
