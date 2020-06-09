# 根据一棵树的中序遍历与后序遍历构造二叉树。
from idlelib.tree import TreeNode
from typing import List


def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    if not inorder:
        return None

    root = TreeNode(postorder[-1])
    i = inorder.index(root.val)
    root.left = self.buildTree(inorder[:i], postorder[:i])
    root.right = self.buildTree(inorder[i+1:], postorder[i:-1])

    return root
