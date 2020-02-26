# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    82. 删除排序链表中的重复元素 II.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/26/20 11:05 PM
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)

def deleteDuplicates(head: ListNode) -> ListNode:
    res, cur, tmp = [], head, None  # 储存node的list
    while cur:
        res.append(cur)
        if cur.next and cur.val == cur.next.val:
            tmp = cur.val
        if cur.val == tmp:
            res.pop()
        cur = cur.next

    res += [None]
    for i in range(len(res)-1):
        res[i].next = res[i+1]
    return res and res[0]

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