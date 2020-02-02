# coding=utf-8
'''
@ Summary: 栈匹配， 先进后出
@ Update:  

@ file:    20. 有效的括号.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/3/20 12:03 AM
'''
def isVaild(s):
    if not s or len(s) < 2:  return False
    # parent = ["()[]{}"]
    opposite = {")":"(", "]":"[", "}":"{"}
    stack = []
    for i in s:
        stack.append(i)  # 入栈
        if i in opposite:
            d_elem = stack.pop()  #出栈
            if not stack or stack.pop() != opposite[d_elem]:
                return False
    return not stack



s = ["]", ")))", "()[]{}", "(]", "([)]", "{[]}"]
[print(isVaild(i)) for i in s]