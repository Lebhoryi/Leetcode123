# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    92. 反转链表 II.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    3/5/20 12:11 AM
'''
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.val)

def reverseBetween(head, m, n):
    if not head:  return

    # 双指针 指到m处开始链表反转
    pre, cur = None, head

    while m > 1:
        pre = cur
        cur = cur.next
        n, m = n - 1, m - 1

    tail, con = cur, pre  # tail 是反转链表的头结点， con 是m前一个节点

    # 链表翻转
    while n:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
        n -= 1

    # link 拼接
    # 头 接 反转链表
    if con:  # 如果m 之前有link
        con.next = pre
    else:
        head = pre

    # 反转链表接 尾
    tail.next = cur  # cur 是n 之后的链表首节点

    return head


def list2link(l):
    # create link
    if not l:  return
    head = ListNode(None)
    move = head
    for i in l:
        tmp = ListNode(i)
        move.next = tmp
        move = move.next
    return head.next

def p_link(head):
    # print link
    if not head:  return
    while head:
        yield head
        head = head.next

if __name__ == "__main__":
    import sys
    _input = list(map(int, sys.stdin.readline().strip().split(",")))
    head = list2link(_input)
    m = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    for node in p_link(reverseBetween(head, m, n)):
        print(node, end=" ")
