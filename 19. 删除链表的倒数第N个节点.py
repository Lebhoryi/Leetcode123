# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    19. 删除链表的倒数第N个节点.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/2/20 10:23 PM
'''
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.val)

def removeNthFromEnd(head, n):
    # # link to list
    # l, cur = [], head
    # while cur:
    #     l.append(cur.val)
    #     cur = cur.next
    # l.pop(-n)
    # # list to link
    # head2 = ListNode(None)
    # move = head2
    # for i in l:
    #     tmp = ListNode(i)
    #     move.next = tmp
    #     move = move.next
    # return head2.next

    # link to list 进阶版
    l = []
    while head:
        l.append(head)
        head = head.next
    if len(l) != n: l[-n-1].next = l[-n].next
    l.pop(-n)
    return l and l[0]

def c_link(l):
    if not l: return
    head = ListNode(0)
    tmp = head
    for i in l:
        node = ListNode(i)
        tmp.next = node
        tmp = tmp.next
    return head.next

def p_link(l):
    if not l:  return
    tmp = l
    while tmp:
        yield tmp.val
        tmp = tmp.next

# l = [i for i in range(1, 6)]
l = [1]
head = c_link(l)
# for node in p_link(head):
#     print(node, end=" ")
n = 1
for node in p_link(removeNthFromEnd(head, n)):
    print(node, end=" ")