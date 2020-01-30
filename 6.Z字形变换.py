# coding=utf-8
'''
@ Summary: 模拟法，关键在于flag
@ Update:  

@ file:    6.Z字形变换.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    1/30/20 1:57 PM
'''
def convert(s, numRows):
    if not s or numRows == 1:  return s

    res = ["" for _ in range(numRows)]  # 存放numRows 行字符串
    i, flag = 0, -1   # i代表行数， flag用于行数变换
    for c in s:  # 迭代字符串s
        res[i] += c  # 按行添加
        # 当遍历到最后一行时，向上或者向下遍历
        if i == 0 or (i+1 - numRows) == 0:
            flag = -flag
        i += flag

    return "".join(res)

        # pass
        # raw[0].aapend(s[0])
        # raw[1].aapend(s[1])
        # raw[2].aapend(s[2])
        # raw[1].append(s[3])
        # raw[0].append(s[4])
        # raw[1].append(s[5])







s = "LEETCODEISHIRING"
num = 4
# s = "LEETCODEISHIRING"
# num = 4
print(convert(s, num))

# L   C   I   R
# E T O E S I I G
# E   D   H   N

# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G