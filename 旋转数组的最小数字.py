# coding=utf-8
"""
https://blog.csdn.net/u010005281/article/details/79823154

@ Summary: 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个非递减排序的数组的一个旋转，输出旋转数组的
最小元素。例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。NOTE：给出的所有元素都大于0，若数组大小为0，
请返回0。
@ Update:  

@ file:    旋转数组的最小数字.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-7-4 下午4:38
"""

def minNumberInRotateArray(arrary):
    left = 0
    right = len(arrary) - 1

    while left < right:
        mid = int((left + right)/2)
        if arrary[mid] > arrary[right]:
            left = mid + 1
        elif arrary[mid] < arrary[right]:
            right = mid
        else:
            right -= 1
    return arrary[left]

a = [3, 4, 5, 1, 2]
print(minNumberInRotateArray(a))