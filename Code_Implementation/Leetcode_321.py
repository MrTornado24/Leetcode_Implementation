# 给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。
#
# 求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。
from typing import List


def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

    def merge(seq1, seq2):
        max_seq = []
        while seq1 and seq2:
            max_seq.append(max(seq1, seq2).pop(0))
        return max_seq+(seq1 or seq2)

    def maxSequence(num, k):
        res = []
        if len(num) < k or k == 0:
            return []
        if k == len(num):
            return num[::]
        pop = len(num) - k
        for i in range(len(num)):
            while res and num[i] > res[-1] and pop > 0:
                res.pop()
                pop -= 1
            res.append(num[i])
        return res[:k]

    temp = []
    for i in range(max(0, k-len(nums2)), min(k, len(nums1))+1):

        temp1 = maxSequence(nums1, i)
        temp2 = maxSequence(nums2, k-i)
        temp = max(merge(temp1, temp2), temp)
    return temp


print(maxNumber(maxNumber, nums1 = [7,3,8,0,6,5,7,6,2], nums2 = [2,5,6,4,4,0], k = 15))


