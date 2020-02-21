# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    63. 不同路径 II.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/21/20 10:39 PM
'''
def uniquePathsWithObstacles(obstacleGrid: [[int]]) -> int:
    dp = obstacleGrid  # 将名称简化，这个名称实在是太长了
    if dp[0][0] == 1:  return 0

    for i in range(len(dp)):  # 行迭代
        for j in range(len(dp[0])):  # 列迭代
            if i == 0 and j == 0:
                dp[i][j] = 1
            elif i == 0 and j >= 1:
                # 检测障碍物是否在首行
                dp[i][j] = 1 if not dp[i][j] and dp[i][j-1] else 0
            elif j == 0 and i >= 1:
                # 检测障碍物是否在首列
                dp[i][j] = 1 if not dp[i][j] and dp[i-1][j] else 0
            else:
                # 如果检测到障碍物，重新赋值为0，不影响下一次计算
                dp[i][j] = 0 if dp[i][j] else dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]

obs = [[0,0,0,0,0],[0,0,0,0,1],[0,0,0,1,0],[0,0,0,0,0]]
print(uniquePathsWithObstacles(obs))