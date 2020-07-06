# 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
# 请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。
import heapq
from collections import Counter
from typing import List
import numpy as np


def kthSmallest(self, matrix: List[List[int]], k: int):
    # 暴力解法，将二维数组转化为一维数组进行排序
    # m = len(matrix)
    # n = len(matrix[0])
    # a = matrix
    # np.reshape(a, (1, -1))
    # matrix_copy = []
    # for i in range(len(a)):
    #     matrix_copy += a[i]
    # return np.sort(matrix_copy)[k-1]

    # 归并排序
    n = len(matrix)
    m = len(matrix[0])
    pq = [(matrix[i][0], i, 0) for i in range(n)]
    heapq.heapify(pq)
    for i in range(k-1):
        num, x, y = heapq.heappop(pq)
        if y != m-1:
            heapq.heappush(pq, (matrix[x][y+1], x, y+1))
    return heapq.heappop(pq)[0]


s = 'hhhhhhello'
print(Counter(s))




print(kthSmallest(kthSmallest, matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
], k = 8,))


