# coding=utf-8
'''
@ Summary: 先获取首列，然后二分类找到这个数所在的行，然后进行判断
@ Update:  

@ file:    74. 搜索二维矩阵.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/24/20 9:59 PM
'''
import bisect
def searchMatrix(matrix: [[int]], target: int) -> bool:
    if not matrix or not matrix[0]:  return False
    col = list(list(zip(*matrix))[0])  # set() -> list()
    index = bisect.bisect_left(col, target, 0, len(matrix)-1)  # 二分查找
    return target in (matrix[index] + matrix[index-1])


matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 16
print(searchMatrix(matrix, target))