# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
# 岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
#
# 此外，你可以假设该网格的四条边均被水包围。
from typing import List

# 深度优先算法，用到了递归


# def dfs(grid, r, c):
#     grid[r][c] = 0
#     rows = len(grid)
#     cols = len(grid[0])
#     neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
#     for neighbor in neighbors:
#         x, y = neighbor[0], neighbor[1]
#         if 0 <= x < rows and 0 <= y < cols and grid[x][y] == "1":
#             dfs(grid, x, y)
#
#
# def numIslands(grid: List[List[str]]) -> int:
#     rows = len(grid)
#     if rows == 0:
#         return 0
#     cols = len(grid[0])
#     count = 0
#     for row in range(rows):
#         for col in range(cols):
#             if grid[row][col] == "1":
#                 count += 1
#                 dfs(grid, row, col)
#     return count


# 广度优先算法，用队列取代递归
# from nltk import collections
#
#
# def numIslands(grid: List[List[str]]) -> int:
#     rows = len(grid)
#     if rows == 0:
#         return 0
#     cols = len(grid[0])
#     count = 0
#     for row in range(rows):
#         for col in range(cols):
#             if grid[row][col] == "1":
#                 count += 1
#                 neighbors = collections.deque([(row, col)])
#                 while neighbors:
#                     r, c = neighbors.popleft()
#                     for x, y in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
#                         if 0 <= x < rows and 0 <= y < cols and grid[x][y] == "1":
#                             neighbors.append((x, y))
#                             grid[x][y] = "0"
#     return count


# 并查集
class UnionFind:
    def __init__(self, grid):
        m, n  = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    def find(self, i):
        while self.parent[i] != i:
            i = self.parent[i]
        return i

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)
        if x != y:
            if self.rank[x] > self.rank[y]:
                x, y = y, x
            self.parent[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
            self.count -= 1

    def getCount(self):
        return self.count


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        count = 0
        uf = UnionFind(grid)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    for neighbor in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                        if neighbor[0] < rows and neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == "1":
                            uf.union(r * n + c, neighbor[0] * n + neighbor[1])

        return uf.getCount()

    print(numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]))