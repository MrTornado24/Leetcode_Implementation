# 给定一个非空二叉树，返回其最大路径和。
#
# 本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        maxPath = None

        def maxpath(node):
            if not node:
                return 0
            maxleft = max(maxpath(node.left), 0)
            maxright = max(maxpath(node.right), 0)
            maxPath = max(maxPath, node.val + maxleft + maxright)
            return node.val + max(maxleft, maxright)

        maxpath(root)
        return maxPath

