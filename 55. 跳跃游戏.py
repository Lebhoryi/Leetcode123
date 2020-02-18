# coding=utf-8
'''
@ Summary: 贪心
@ Update:

思路：尽可能到达最远位置（贪心）。
如果能到达某个位置，那一定能到达它前面的所有位置。

方法：初始化最远位置为0，然后遍历数组，如果当前位置能到达，并且当前位置+跳数>最远位置，就更新最远位置。最后比较最远位置和数组长度。

复杂度：时间复杂度O(n)，空间复杂度O(1)。

作者：mo-lan-4
链接：https://leetcode-cn.com/problems/jump-game/solution/pythonji-bai-97kan-bu-dong-ni-chui-wo-by-mo-lan-4/

@ file:    55. 跳跃游戏.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/19/20 12:26 AM
'''

def canJump(nums: [int]) -> bool:
    max_i = 0  # 该点能跳到的最远的位置
    for i, jump in enumerate(nums):
        # 如果当前位置能到达，并且当前位置+跳数>最远位置
        if max_i >= i and max_i < i + jump:
            max_i = i + jump #更新最远能到达位置
        # if max_i >= len(nums): break
    return max_i >= i


nums = [0]
print(canJump(nums))