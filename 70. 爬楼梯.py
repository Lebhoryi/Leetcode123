# coding=utf-8
'''
@ Summary: DP, dp[i] = dp[i-1] + dp[i-2]; 斐波那契
@ Update:  

@ file:    70. 爬楼梯.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/23/20 10:10 PM
'''
def climbStairs(n: int) -> int:
    # 超时
    # if n <= 2:  return n
    # return climbStairs(n-1) + climbStairs(n-2)

    # 时间复杂度 O(n) 空间复杂度 O(n)
    dp = [0] * n
    for i in range(n):
        dp[i] = dp[i-1] + dp[i-2] if i > 1 else i + 1
    return dp[-1]

    # 进阶版斐波那契
    # a, b = 0, 1
    # while n > 0:
    #     a, b = b, a + b
    #     n -= 1
    # return b

n = 2
print(climbStairs(n))