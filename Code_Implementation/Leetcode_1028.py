# 我们从二叉树的根节点 root 开始进行深度优先搜索。
#
# 在遍历中的每个节点处，我们输出 D 条短划线（其中 D 是该节点的深度），然后输出该节点的值。（如果节点的深度为 D，则其直接子节点的深度为 D + 1。根节点的深度为 0）。
#
# 如果节点只有一个子节点，那么保证该子节点为左子节点。
#
# 给出遍历输出 S，还原树并返回其根节点 root。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def recoverFromPreorder(self, S: str) -> TreeNode:
    # path = list()
    # i = 0
    # while i < len(S):
    #     depth = 0
    #     while S[i] == "-" and i < len(S):
    #         depth += 1
    #         i += 1
    #     value = 0
    #     while i < len(S) and S[i].isdigit():
    #         value = value * 10 + (ord(S[i]) - ord('0'))
    #         i += 1
    #     node = TreeNode(value)
    #     if depth == len(path):
    #         if path:
    #             path[-1].left = node
    #     else:
    #         path = path[:depth]
    #         path[-1].right = node
    #     path.append(node)
    # return path[0]

    path, pos = list(), 0
    while pos < len(S):
        level = 0
        while S[pos] == '-':
            level += 1
            pos += 1
        value = 0
        while pos < len(S) and S[pos].isdigit():
            value = value * 10+(ord(S[pos])-ord('0'))
            pos += 1
        node = TreeNode(value)
        if level == len(path):
            if path:
                path[-1].left = node
        else:
            path = path[:level]
            path[-1].right = node
        path.append(node)
    print(len(path))
    return path[0]


print(recoverFromPreorder(recoverFromPreorder, "1-2--3--4-5--6--7"))









