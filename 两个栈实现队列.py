# coding=utf-8
'''
https://github.com/leeguandong/Interview-code-practice-python/blob/master/%E5%89%91%E6%8C%87offer/%E4%B8%A4%E4%B8%AA%E6%A0%88%E5%AE%9E%E7%8E%B0%E9%98%9F%E5%88%97.py#L16

@ Summary: 用两个栈来实现一个队列，完成队列的Push和Pop操作
@ Update:  

@ file:    两个栈实现队列.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    6/29/19 4:38 PM
'''
'''
题目：用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''

'''
这一题还是挺难的，有两个栈stackA、stackB，A是入栈的，B是出栈的，入栈时，直接进入A即可，出栈时，先判断是否有元素，
如果B没有元素，pop肯定报错，应该先将A中所有的元素压倒B里面，再pop最上面一个元素，如果B中有就直接pop出，就可以，
这是最优的思路，两个栈实现了先进后出，在一起又实现了队列的先进先出。
23ms
5628k
'''

class MyQueue(object):
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, node):
        self.stackA.append(node)

    def pop(self):
        if self.stackB:
            return self.stackB.pop()
        while self.stackA:
            # 入栈
            self.stackB.append(self.stackA.pop())
        return self.stackB.pop() if self.stackB else "The queue is empty..."

if __name__ == '__main__':
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.pop())
    print(q.pop())

    q.push(3)
    print(q.pop())
    q.push(4)
    print(q.pop())
    print(q.pop())
    print(q.pop())
