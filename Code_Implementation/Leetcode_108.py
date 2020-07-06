# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
#
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List


def sortedArrayToBST(nums: List[int]) -> TreeNode:
    def buildTree(nums, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = buildTree(nums[:mid], left, mid-1)
        root.right = buildTree(nums[mid+1:], mid+1, right)
        return root
    return buildTree(nums, 0, len(nums) - 1)


res = set()
res.add((1,2,3))
print(res)
res.add((1,2,3))
print(res)
