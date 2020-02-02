# coding=utf-8
'''
@ Summary: 递归
@ Update:  

@ file:    21. 合并两个有序链表.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/3/20 12:28 AM
'''
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.val)

def mergeTwoLists(l1, l2):
    if l1 and l2:
        if l1.val > l2.val:  l1, l2 = l2, l1
        l1.next = mergeTwoLists(l1.next, l2)
    return l1 or l2

def c_link(link):
    if not link:  return
    head = ListNode(None)
    move = head
    for i in link:
        tmp = ListNode(i)
        move.next = tmp
        move = move.next
    return head.next

def p_link(head):
    if not head:  return
    tmp = head
    while tmp:
        yield tmp
        tmp = tmp.next
    print()

l1 = [1, 2, 5, 8]
l2 = [1, 3, 4]
l1 = c_link(l1)
# for node in p_link(l1):
#     print(node, end=" ")
l2 = c_link(l2)
for node in p_link(mergeTwoLists(l1, l2)):
    print(node, end=" ")