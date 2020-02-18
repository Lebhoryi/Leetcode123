# coding=utf-8
'''
@ Summary: 递归
@ Update:  

@ file:    54. 螺旋矩阵.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/17/20 9:36 PM
'''
def spiralOrder(matrix: [[int]]) -> [int]:
    # print(matrix.pop(0))
    # 为什么是[*matrix.pop(0)]
    # 而不是matrix.pop(0)？因为对于后面的递归，传进来的列表中元素是tuple
    # 最后是 [(3,)] 这样的格式，需要先解包，转化成list
    # if len(matrix) == 1:  return list(*matrix)
    return matrix and [*matrix.pop(0)] + spiralOrder(list(zip(*matrix))[::-1])

matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
# matrix = []
print(spiralOrder(matrix))