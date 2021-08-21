# coding=utf-8
'''
https://github.com/JushuangQiao/Python-Offer

@ Summary: 从尾到头打印单链表
            思路：递归
@ Update:  

@ file:    6.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    6/27/19 6:45 PM
'''

class LinkNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return str(self.val)

class CreateLink(object):

    @staticmethod
    def link(vals):
        head = LinkNode(len(vals))
        # print(head.val)
        # print(head.next)
        move = head
        if vals:
            for val in vals:
                tmp = LinkNode(val)
                move.next = tmp
                move = tmp
        return head.next

def print_link_inverse(links):
    if links:
        print_link_inverse(links.next)
        print(links.val)

# link_a = [1, 2, 3, 4, 5]
link_a = {67,0,24,58}
# link_a = list(link_a)
link_a = CreateLink().link(link_a)
print_link_inverse(link_a)
