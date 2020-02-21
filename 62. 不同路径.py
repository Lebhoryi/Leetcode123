# coding=utf-8
'''
@ Summary: dp, dp[i][j] = dp[i-1][j] + dp[i][j-1]
@ Update:  

@ file:    62. 不同路径.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/21/20 10:03 PM
'''
def uniquePaths(m: int, n: int) -> int:
    # # 空间复杂度 n^2
    # dp = [[0] * n for _ in range(m)]
    # for i in range(m):
    #     for j in range(n):
    #         dp[i][j] = 1 if i == 0 or j == 0 else dp[i-1][j] + dp[i][j-1]
    # return dp[-1][-1]

    # 优化 空间复杂度
    dp = [1] * n
    for i in range(1, m):
        for j in range(1, n):
            dp[j] = dp[j-1] + dp[j]
    return dp[-1]

m, n = 3, 3
print(uniquePaths(m, n))