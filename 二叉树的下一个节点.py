# coding=utf-8
'''
https://github.com/leeguandong/Interview-code-practice-python/blob/master/%E5%89%91%E6%8C%87offer/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E4%B8%8B%E4%B8%80%E4%B8%AA%E8%8A%82%E7%82%B9.py

@ Summary: 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右
子结点，同时包含指向父结点的指针。
@ Update:  

@ file:    二叉树的下一个节点.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    6/29/19 3:15 PM
'''

'''
题目：给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右
子结点，同时包含指向父结点的指针。
'''

'''
思路：
（1） 若该节点存在右子树：则下一个节点为右子树最左子节点,遍历
（2） 若该节点不存在右子树：这时分两种情况：
 2.1 该节点为父节点的左子节点，则下一个节点为其父节点
 2.2 该节点为父节点的右子节点，则沿着父节点向上遍历，知道找到一个节点的父节点的左子节点为该节点，
 则该节点的父节点下一个节点（如图节点I，沿着父节点一直向上查找找到B（B为其父节点的左子节点），
 则B的父节点A为下一个节点）。
34ms
5632k
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class NextNode(object):
    def next_node(self, pNode):
        if not pNode:
            return None
        # 该节点有右子节点，那么该节点的下一个节点就是右子树的最左节点
        if pNode.right:
            pNode = pNode.right
            while not pNode.left:
                pNode = pNode.left
            return pNode
        # 该节点没有右子节点
        # 该节点为父节点的左子节点,下一个节点为父节点
        elif pNode.next and pNode.next.left == pNode:
            return pNode.next
        # 该节点为父节点的右子节点，它的下一个节点就是其父节点作为父节点的左子节点的下一个节点
        elif pNode.next and pNode.next.right == pNode:
            pNode = pNode.next
            while pNode.next and pNode.next.left != pNode:
                pNode = pNode.next
            return pNode
        else:
            # 节点无父节点，即节点为根节点
            return pNode.next

