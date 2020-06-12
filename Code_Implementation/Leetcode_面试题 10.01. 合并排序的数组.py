# 给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。
#
# 初始化 A 和 B 的元素数量分别为 m 和 n。
from typing import List


def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
    # lenA = len(A)
    # lenB = len(B)
    # for i in range(lenA-lenB, lenA):
    #     A[i] = B[i-lenA+lenB]
    # A.sort()
    # print(A)
    A[m:] = B
    A.sort()


merge(merge, A = [1,2,3,0,0,0], m = 3, B = [2,5,6], n = 3)