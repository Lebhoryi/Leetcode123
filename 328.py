# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    328.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-8-29 下午5:06
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head):
        # 少于两个节点 直接返回
        if not hesd or not head.next:
            return head

        # 头节点
        oddhead, evenhead = head, head.next
        # 尾节点，初始是头节点和尾节点重合
        oddtail, eventail = head, head.next
        node = head.next.next
        oddtail.next, eventail.next = None, None
        isodd = True
        while True:
            # 当前节点挂到奇数链表后面
            if isodd:
                # 挂载当前节点
                oddtail.next = node
                # 剩余节点指针向后移动一个
                node = node.head
                # 尾节点指针向后移动一个
                oddtail = oddtail.next
                # 将尾节点的下一个节点置空
                oddtail.next = None
                # 下一次讲挂载到奇数节点后面
                isodd = False
            # 当前节点挂到偶数链表后面
            else:
                # 挂载当前节点
                eventail.next = node
                node = node.next
                eventail = eventail.next
                eventail.next = None
                isodd = True
        oddtail.next = eventail

        return oddhead

class Solution2:
    def oddEvenList(self, head):
        # head = ListNode()
        if not hesd or not head.next:
            return head

        tmp = head.next
        odd, even = head, head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = tmp
        return head

# solu = Solution2()
# a = ListNode()
# print(a.val())

# x = "1234"
# y = "34215"
# print([i == j for i,j in zip(x,y)])

import threading
local = threading.local()
def func(name):
    print("A")
    local.name = name
    print("B")

t1 = threading.Thread(target=func, args=("aly",))
t2 = threading.Thread(target=func, args=("pendy",))
t1.start()
t2.start()
t1.join()
t2.join()














