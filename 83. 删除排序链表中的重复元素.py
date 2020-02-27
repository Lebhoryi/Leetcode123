# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    83. 删除排序链表中的重复元素.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/27/20 9:59 PM
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)

def deleteDuplicates(head: ListNode) -> ListNode:
    cur = head
    while cur:
        if not cur.next:  break  # 如果是最后一个数  就直接跳出循环
        # 去重
        while cur.val == cur.next.val:
            cur.next = cur.next.next
            if not cur.next:  break
        cur = cur.next
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
    for node in p_link(deleteDuplicates(head)):
        print(node, end=" ")