# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    扑克牌问题.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    9/28/19 10:57 PM
'''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.val)

class LCLink(object):
    @ staticmethod
    def c_link(vals):
        # Create link
        if not vals:
            return None
        head = Node(len(vals))  # head node
        move = head  # moving node
        for i in range(len(vals)):
            tmp = Node(vals[i])
            tmp.next = tmp if i == 0 else move.next
            move.next = tmp
            move = tmp
        return move

    @ staticmethod
    def p_link(link):
        # print link
        if not link:
            return None
        cur = link.next
        while cur.next != link.next:
            yield cur.val
            cur = cur.next
        yield cur.val

    @ staticmethod
    def l_link(link):
        # lenth of link
        if not link:
            return None
        cur, count = link.next, 1
        while cur.next != link.next:
            count += 1
            cur = cur.next
        return count

    @ staticmethod
    def res_link(link, s):
        # 第s+1个节点作为首节点
        if not link:
            return None
        cur, count = link.next, 1
        if s != 1:
            while count < s:  # 找到第s-1个点
                cur = cur.next
                count += 1
        return cur



def is_zero(link):
    # 判断link.val是否是0
    if not link:
        return None
    if link.next.val != 0:
        return link.next
    else:
        return link


def magic(link, s):
    if not link:
        return None
    count = 1
    cur = link
    for i in range(1, s+1):
        cur.next.val = i + 10
        print("The link changed:", end=" ")
        for node in LCLink.p_link(cur):
            print(node, end=" ")
        print()

        print("Rest link:", end=" ")
        cur = LCLink.res_link(cur, i+1)
        for node in LCLink.p_link(cur):
            print(node, end=" ")
        print()
        print("=" * 25)
        while cur.next.val != 0:
            cur = cur.next
        for node in LCLink.p_link(cur):
            print(node, end=" ")
        print()
        print("=" * 25)

    return cur





if __name__ == "__main__":
    s = 5
    _list = [0] * s
    # _list = list(range(1, s))
    # print(_list)
    link = LCLink.c_link(_list)
    print("The origin link is:", end=" ")
    for node in LCLink.p_link(link):
        print(node, end=" ")
    print()
    print("="*25)

    # 从第s个位置重置link
    # s = 2
    # link = LCLink.res_link(link, s)
    # for node in LCLink.p_link(link):
    #     print(node, end=" ")
    # print()
    # print("="*25)

    # link.next.val = 1
    # print("The link changed:", end=" ")
    # for node in LCLink.p_link(link):
    #     print(node, end=" ")
    # print()
    # print("="*25)
    # print("Rest link:", end=" ")
    # link = LCLink.res_link(link, 1)
    # for node in LCLink.p_link(link):
    #     print(node, end=" ")
    # print()
    # print("="*25)
    #
    # link.next.next.val = 2
    # print("The link changed:", end=" ")
    # for node in LCLink.p_link(link):
    #     print(node, end=" ")
    # print()
    # print("=" * 25)
    # print("Rest link:", end=" ")
    # link = LCLink.res_link(link, 2)
    # for node in LCLink.p_link(link):
    #     print(node, end=" ")
    # print()
    # print("=" * 25)
    #
    # link.next.next.next.next.val = 3
    # print("The link changed:", end=" ")
    # for node in LCLink.p_link(link):
    #     print(node, end=" ")
    # print()
    # print("=" * 25)
    # print("Rest link:", end=" ")
    # link = LCLink.res_link(link, 3)
    # for node in LCLink.p_link(link):
    #     print(node, end=" ")
    # print()
    # print("=" * 25)

    magic_link = magic(link, s)
    # for node in LCLink.p_link(magic_link):
    #     print(node, end=" ")
    # print()
    # print("="*25)

