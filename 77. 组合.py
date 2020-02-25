# coding=utf-8
'''
@ Summary: dfs
@ Update:  

@ file:    77. 组合.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/25/20 10:50 PM
'''
def combine(n: int, k: int) -> [[int]]:

    # # 可行，但是时间复杂度比较大
    # n_list, path, res = [*range(1, n+1)], [], []
    # def dfs(n_list, path):
    #     # 终止条件
    #     if len(path) == k:
    #         res.append(path[:])
    #
    #     # 梦开始的地方
    #     for i in range(len(n_list)):
    #         dfs(n_list[i+1:], path + [n_list[i]])
    # dfs(n_list, path)
    # return res

    # 内置函数
    from itertools import combinations
    n_list = [*range(1, n+1)]
    # print(n_list)
    return list(map(list, combinations(n_list, k)))

n = 4
k = 2
print(combine(n, k))