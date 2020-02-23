# coding=utf-8
'''
@ Summary: 栈
@ Update:  

@ file:    71. 简化路径.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/23/20 11:19 PM
'''
def simplifyPath(path: str) -> str:
    res = []
    for i in path.split("/"):
        # res.append(i)
        # res = {"": res, ".": res, "..": res[:-1]}.get(i, res + [i])
        if i not in {"", ".", ".."}:
            res.append(i)
        elif i == ".." and res:
            res.pop()
    return res

path = "/home/"
path = "/../"
path = "/home//foo/"
path = "/a/./b/../../c/"
path = "/a/../../b/../c//.//"
path = "/a//b////c/d//././/.."
print(simplifyPath(path))

