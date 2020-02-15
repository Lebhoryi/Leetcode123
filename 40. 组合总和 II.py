# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    40. 组合总和 II.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/11/20 2:42 PM
'''


class Solution:
    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
        if not candidates:  return []
        path, res, candidates = [], [], sorted(candidates)

        def dfs(candidates, begin, end, path, target):
            if target == 0:
                # if path[:] not in res:
                res.append(path[:])

            for i in range(begin, end):
                residue = target - candidates[i]
                # break 是后续遍历不执行，continue 继续执行后续遍历
                if residue < 0:
                    break
                # 与39不一样的是这一步 去重
                if i > begin and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                dfs(candidates, i + 1, end, path, residue)
                path.pop()

        dfs(candidates, 0, len(candidates), path, target)
        return res

candidates = [10,1,2,7,6,1,5]
target = 8
solution = Solution()
print(solution.combinationSum2(candidates, target))