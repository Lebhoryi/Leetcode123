# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    48. 旋转图像.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/15/20 11:06 PM
'''

def rotate(matrix: [[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    # col = [i for i in zip(*matrix)]
    # # print("col: {}".format(col))
    # for i in range(len(matrix)):
    #     matrix[i] = col[i][::-1]

    for i in range(len(matrix[0])):
        for j in range(i, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in len(matrix):
        matrix[i][::-1]


matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
rotate(matrix)
print("matrix: {}".format(matrix))