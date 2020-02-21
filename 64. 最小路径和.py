# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    64. 最小路径和.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/21/20 11:57 PM
'''


def minPathSum(grid: [[int]]) -> int:
    # dp = [[0] * len(range(len(grid[0]))) for _ in range(len(grid))]
    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         if i == 0 and j == 0:
    #             dp[i][j] = grid[i][j]
    #         elif i == 0 and j >= 1:
    #             dp[i][j] = grid[i][j] + dp[i][j-1]
    #         elif j == 0 and i >= 1:
    #             dp[i][j] = grid[i][j] + dp[i-1][j]
    #         else:
    #             dp[i][j] = min(grid[i][j] + dp[i-1][j], grid[i][j] + dp[i][j-1])
    # return dp[-1][-1]

    # 上面的内存复杂度是n^2 ， 魔改成n
    dp = [0 for _ in range(len(grid[0]))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0 and j == 0:
                dp[j] = grid[i][j]
            elif i == 0 and j > 0:  # 首行
                dp[j] = grid[i][j] + dp[j-1]
            elif j == 0 and i > 0:  # 首列
                dp[j] = grid[i][j] + dp[j]
            else:
                dp[j] = grid[i][j] + min(dp[j-1], dp[j])
    return dp[-1]

grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(minPathSum(grid))