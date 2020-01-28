# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    2.两数相加.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    1/28/20 1:49 PM
'''
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.val)


def addTwoNumber(l1, l2):
    head = ListNode(0)
    tmp = head  # 创建一个链表
    carry = 0  # 十进制进位
    while l1 or l2:
        s = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
        carry = s // 10  # 十进制进位
        # 新链表节点赋值
        tmp.next = ListNode(s%10)
        tmp = tmp.next

        # l1, l2 指向下一个元素
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    # 如果链表最后两个数相加大于0，则补上最后一个进位
    if carry > 0:
        tmp.next = ListNode(carry)

    return head.next


def listtolink(l):
    if not l:  return l
    head = ListNode(0)
    tmp = head
    for elem in l:
        tmp.next = ListNode(elem)
        tmp = tmp.next
    return head.next

def p_link(link):
    if not link:  return []
    cur = link
    while cur:
        yield cur.val
        cur = cur.next

list1 = [2, 4, 3]
list2 = [5, 6, 4]
l1 = listtolink(list1)
l2 = listtolink(list2)

for node in p_link(addTwoNumber(l1, l2)):
    print(node, end=" ")



