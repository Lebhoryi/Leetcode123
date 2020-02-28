# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    89. 格雷编码.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/29/20 12:12 AM
'''
def grayCode(n: int) -> [int]:
    res, head = [0], 1
    for i in range(n):
        for j in res[::-1]:
            # 镜像翻转，res是上半部，现增加下半部
            # 下半部 = 2^i + 上半部逆序
            res.append(head + j)
        # << 左移符号，即在二进制表示后加一位 0
        # 例子：1 << i 等于 1 * 2^i
        head <<= 1
    return res

n = 3
print(grayCode(n))