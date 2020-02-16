# coding=utf-8
'''
@ Summary: 字典，{set():[]}
@ Update:  

@ file:    49. 字母异位词分组.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/17/20 12:02 AM
'''
def groupAnagrams(strs: [str]) -> [[str]]:
    d = {}
    for s in strs:
        k = "".join(sorted(s))
        d[k] = d.get(k, []) + [s]
    return list(d.values())


d = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(d))