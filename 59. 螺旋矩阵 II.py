# coding=utf-8
'''
@ Summary: 
@ Update:  github.com/cy69855522/Shortest-LeetCode-Python-Solutions

@ file:    59. 螺旋矩阵 II.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/19/20 10:39 PM
'''
def generateMatrix(n: int) -> [[int]]:
    res, n = [[n ** 2]], n ** 2
    while n > 1:
        # 逆向思考，从中心散发一点到最外圈
        # 最上边 + 之前res 顺时针旋转90度
        n, res = n - len(res), [[*range(n-len(res), n)]] + list(zip(*res[::-1]))
    return res

n = 3
print(generateMatrix(n))