# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    60. 第k个排列.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/19/20 11:35 PM
'''
import itertools

def getPermutation(n: int, k: int) -> str:
    # 方法一 内置函数
    # res = list(itertools.permutations([*range(1, n+1)]))[k-1]
    # return "".join(list(map(lambda x: str(x), res)))

    n, res, path = [*range(1, n + 1)], [], []
    def dfs(n, path):
        if len(res) == k:
            return
        if len(n) == 0:
            res.append(path[:])
        for i in range(len(n)):
            dfs(n[:i] + n[i+1:], path + [n[i]])
    dfs(n, path)
    return "".join(list(map(lambda x: str(x), res[-1])))

n = 3
k = 3
print(getPermutation(n, k))