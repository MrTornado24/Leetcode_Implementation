# 根据一棵树的前序遍历与中序遍历构造二叉树。
from idlelib.tree import TreeNode
from typing import List


def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    if not preorder:
        return None
    root = TreeNode(preorder[0])
    i = inorder.index(root.val)
    root.left = self.buildTree(preorder[1:i+1], inorder[:i])
    root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
    return root

