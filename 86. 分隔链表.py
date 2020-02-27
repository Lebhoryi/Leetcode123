# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    86. 分隔链表.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/27/20 11:07 PM
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)

def partition(head: ListNode, x: int) -> ListNode:
    # 比x小的小表表头 比x大的大表表头
    min_link_head, max_link_head = ListNode(None),  ListNode(None)
    # 小表节点 大表节点
    min_link, max_link = min_link_head, max_link_head
    while head:
        if head.val < x:
            min_link.next = head
            min_link = min_link.next
        else:
            max_link.next = head
            max_link = max_link.next
        head = head.next
    # 手动给定，否则溢出
    max_link.next = None
    # 两表拼接
    min_link.next = max_link_head.next
    return min_link_head.next

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
    x = int(sys.stdin.readline())
    for node in p_link(partition(head, x)):
        print(node, end=" ")