# coding=utf-8
'''
@ Summary: Pown(x, n)
@ Update:  https://leetcode-cn.com/problems/powx-n/

@ file:    50. Pow(x, n).py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-11-15 下午4:49
'''
def myPow(x, n):
    if not n: return 1
    if n == 1: return x
    if n < 0:  return 1/myPow(x, -n)
    if n % 2:  return x * myPow(x, n-1)
    return myPow(x*x, n/2)


if __name__ == "__main__":
    x, n = 2.10000, 3
    print(myPow(x, n))