'''
求和

Date:2019/02/25
'''

class Solution(object):
    '''求和

    '''
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def twoSum(self,):
        if not self.nums:  return self.nums

        dic = {}
        for index, item in enumerate(self.nums):
            # 拿到一个值先判断另外一个值是否在字典中，高效，避免遍历全部
            if (self.target - item) in dic:  # 如果有在字典中，返回字典对应的value值，和现在的索引值
                return dic[self.target - item], index
            dic[item] = index  # 只能判断key 是否在dict，不能判断value

nums = [2, 7, 11, 15]
target = 9

solu = Solution(nums, target)
print(solu.twoSum())
