# coding=utf-8
'''
@ Summary: 递归
@ Update:  

@ file:    24. 两两交换链表中的节点.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/3/20 9:53 PM
'''
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.val)

def swapPairs(head):
    if head and head.next:
        head.next.next, head.next, head = head, swapPairs(head.next.next), head.next
    return head

def c_link(lists):
    if not lists:  return
    head = ListNode(0)
    move  = head
    for i in lists:
        tmp = ListNode(i)
        move.next = tmp
        move = move.next
    return head.next

def p_link(link):
    if not link:  return
    tmp = link
    while tmp:
        yield tmp
        tmp = tmp.next
    print()


lists = [1, 2, 3, 4]
head = c_link(lists)
# print(head.next.next)
for node in p_link(swapPairs(head)):
    print(node, end=" ")