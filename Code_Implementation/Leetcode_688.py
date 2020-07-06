# 已知一个 NxN 的国际象棋棋盘，棋盘的行号和列号都是从 0 开始。即最左上角的格子记为 (0, 0)，最右下角的记为 (N-1, N-1)。 
#
# 现有一个 “马”（也译作 “骑士”）位于 (r, c) ，并打算进行 K 次移动。 
#
# 如下图所示，国际象棋的 “马” 每一步先沿水平或垂直方向移动 2 个格子，然后向与之相垂直的方向再移动 1 个格子，共有 8 个可选的位置。
import functools


def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
    # 递归思想，但超时
    # rows = N
    # cols = N
    #
    # def find(r, c, K):
    #     if r >= rows or c >= cols or r < 0 or c < 0:
    #         return 0
    #     if K <= 0:
    #         return 1
    #     count = 0
    #     positions = [(1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1), (-1, -2), (-2, -1)]
    #     for position in positions:
    #         row = r + position[0]
    #         col = c + position[1]
    #         if 0 <= row < rows and 0 <= col < cols:
    #                 count += find(row, col, K-1)
    #
    #         else:
    #             continue
    #     return count
    #
    # count = find(r, c, K)
    # return count / (8 ** K)

    # 递归，改进
    @functools.lru_cache(None)
    def dfs(r, c, counts):
        if r < 0 or r > N-1 or c < 0 or c > N-1:
            return 0
        if counts == K:
            return 1

        step = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

        res = 0

        for i, j in step:
            res += dfs(r+i, c+j, counts+1)

        return res / 8

    return dfs(r, c, 0)


print(knightProbability(knightProbability, 3, 2, 0, 0))


