# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    61. 旋转链表.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2/20/20 10:14 PM
'''
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.val)

def rotateRight(head: ListNode, k: int) -> ListNode:
    # 自己拍脑袋 link to list to link
    # res = []
    # while head:
    #     res.append(head.val)
    #     head = head.next
    # if not res:  return
    # k %= len(res)
    # res = res[-k:] + res[:-k] if k else res
    # head = ListNode(None)
    # move = head
    # for i in res:
    #     tmp = ListNode(i)
    #     move.next = tmp
    #     move = tmp
    # return head.next

    # 把节点直接存储进列表，我之前的思路是把node的val存储进节点
    # 效果差不多，但是代码好看
    res = []
    while head:
        res, head = res + [head], head.next
    if res:
        k %= len(res)
        res[-1].next = res[0]
        res[-k-1].next =  None
    return res[-k] if res else None

def creat_link(l):
    if not l:  return
    head = ListNode(None)
    move = head
    for i in l:
        node = ListNode(i)
        move.next = node
        move = move.next
    return head.next

def print_link(head):
    if not head:  return
    while head:
        yield head
        head = head.next


_list = [*range(1, 6)]
k = 2
for node in (print_link(rotateRight(creat_link(_list), k))):
    print(node, end=" ")