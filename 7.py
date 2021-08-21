# coding=utf-8
'''
https://github.com/JushuangQiao/Python-Offer
https://blog.csdn.net/flannery023/article/details/80885098

@ Summary:
要求：用前序和中序遍历结果构建二叉树，遍历结果中不包含重复值
思路：前序的第一个元素是根结点的值，在中序中找到该值，中序中该值的左边的元素是根结点的左子树，右边是右子树，然后递归的处理左边和右边
提示：二叉树结点，以及对二叉树的各种操作
@ Update:  

@ file:    7.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    6/27/19 7:07 PM
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree(object):
    def construct_tree(self, pre, tin):
        if not pre:
            return None
        elif len(pre) == 1:
            root = TreeNode(pre[0])
        else:
            root = TreeNode(pre[0])
            # 左子树 和 右子树
            root.left = self.construct_tree(pre[1:tin.index(pre[0])+1], tin[:tin.index(pre[0])])
            root.right = self.construct_tree(pre[tin.index(pre[0])+1:], tin[tin.index(pre[0])+1:])
        return root
    

if __name__ == '__main__':
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]
    t = Tree()
    root = t.construct_tree(pre, tin)
    print(root)