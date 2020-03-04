# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    91. 解码方法.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    3/2/20 9:50 PM
'''

def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    # char, d = [chr(i) for i in range(65, 65+26)], {}
    # for i in range(len(char)):
    #     d[i] = char[i]
    pp, p = 1, int(s[0] != '0')
    for i in range(1, len(s)):
        pp, p = p, pp * (9 < int(s[i-1:i+1]) <= 26) + p * (int(s[i]) > 0)
    return p


if __name__ == "__main__":
    import sys
    s = sys.stdin.readline().strip()
    print(numDecodings(s))

