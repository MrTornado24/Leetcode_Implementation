# 这里有一幅服务器分布图，服务器的位置标识在 m * n 的整数矩阵网格 grid 中，1 表示单元格上有服务器，0 表示没有。
#
# 如果两台服务器位于同一行或者同一列，我们就认为它们之间可以进行通信。
#
# 请你统计并返回能够与至少一台其他服务器进行通信的服务器的数量。
from typing import List
import numpy as np


def countServers(self, grid: List[List[int]]) -> int:
    # 每次计算元素所在行和列之和，计算时间较长
    # rows = len(grid)
    # cols = len(grid[0])
    # count = 0
    # for row in range(rows):
    #     for col in range(cols):
    #         numNeighbor = 0
    #         if grid[row][col] == 1:
    #             if sum(grid[row]) > 1 or np.sum(grid, axis=0)[col] > 1:
    #                 numNeighbor += 1
    #         else:
    #             continue
    #         if numNeighbor > 0:
    #             count += 1
    # return count

    # 先将每行和列的主机数量统计好，减少重复运算量
    rows = len(grid)
    cols = len(grid[0])
    count_row = [0] * rows
    count_col = [0] * cols
    count = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                count_row[row] += 1
                count_col[col] += 1
    for row in range(rows):
        for col in range(cols):
            if (count_col[col] > 1 or count_row[row] > 1) and grid[row][col] == 1:
                count += 1
    return count


print(countServers(countServers, grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]))
