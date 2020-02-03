# coding=utf-8
'''
@ Summary: 递归
@ Update:  

@ file:    22. 括号生成.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/3/20 2:59 PM
'''
def generateParenthesis(n):
    if n == 0:
        return [""]
    elif n == 1:
        return ["()"]
    elif n == 2:
        return ["(())", "()()"]

    res = []
    for i in range(n):
        j = n - 1 - i
        tmp1 = generateParenthesis(i)
        tmp2 = generateParenthesis(j)
        res.extend(["(%s)%s" % (p,q) for p in tmp1 for q in tmp2])
    return res


n = 3
print(generateParenthesis(n))