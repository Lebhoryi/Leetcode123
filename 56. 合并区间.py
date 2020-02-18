# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    56. 合并区间.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/19/20 12:47 AM
'''
def merge(intervals: [[int]]) -> [[int]]:
    if len(intervals) < 2:  return intervals
    # 先排序， 在进行计算
    res, intervals  =[], sorted(intervals, key=lambda x: x[0])

    for i in range(len(intervals)):
        if not res or res[-1][1] < intervals[i][0]:
            res.append(intervals[i])
        else:
            res[-1][1] = max(res[-1][1], intervals[i][1])
    return res
    # res = [intervals[0]]
    # def tmp(intervals):
    #     if len(intervals) < 1: return
    #     if res[-1][1] < intervals[0][0] or res[-1][0] > intervals[0][1]:
    #         res.append(intervals[0])
    #     else:
    #         res[-1] = [min(res[-1][0], intervals[0][0]), max(res[-1][1], intervals[0][1])]
    #     tmp(intervals[1:])

    # tmp(intervals[1:])
    # return res


# intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals = [[1,4],[0,2],[3,5]]
# intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
print(merge(intervals))

