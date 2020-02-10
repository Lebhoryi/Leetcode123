# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    39. 组合总和.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/8/20 10:36 PM
'''
def combinationSum(candidates: [int], target: int) -> [[int]]:
    if not candidates: return []
    # path 遍历过程中的路径
    path, res, candidates = [], [], sorted(candidates)
    def dfs(candidates, begin, end, path, target):
        # 终止条件
        if target == 0:
            # Python 中可变对象是引用传递，因此需要将当前 path 里的值拷贝出来
            # 否则res跟着path值更改
            res.append(path[:])
            # print("res: {}".format(res))

        for i in range(begin, end):
            residue = target - candidates[i]  #　更新传入下一个递归的target
            # candidates中大于target之后的值尽不参与递归，剪枝
            if residue < 0:
                break
            # 记录path
            path.append(candidates[i])
            # 遍历大于等于candidates[i]的数，小于该值的不进行遍历，剪枝
            dfs(candidates, i, end, path, residue)
            path.pop()


    dfs(candidates, 0, len(candidates), path, target)
    return res


candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates, target))