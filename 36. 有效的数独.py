# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    36. 有效的数独.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/7/20 9:05 PM
'''
def isValidSudoku(board: [[str]]) -> bool:
    '''
    1. 行中没有重复的数字。
    2. 列中没有重复的数字。
    3. 3 x 3 子数独内没有重复的数字。
    '''
    row = [[i for i in j if i != "."] for j in board]
    col = [[i for i in j if i != "."] for j in zip(*board)]
    pal = [[board[i+x][j+y] for i in range(3) for j in range(3)
            if board[i+x][j+y] != "."] for x in (0, 3, 6) for y in (0, 3, 6)]

    return all(len(set(i)) == len(i) for i in (*row, *col, *pal))


board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

print(isValidSudoku(board))