# 给你一个非递减的 有序 整数数组，已知这个数组中恰好有一个整数，它的出现次数超过数组元素总数的 25%。
#
# 请你找到并返回这个整数

from typing import List


def findSpecialInteger(self, arr: List[int]) -> int:
    # 哈希表统计每个元素出现次数
    dct = {}
    for i, ch in enumerate(arr):
        if ch not in dct:
            dct[ch] = 1
        else:
            dct[ch] += 1
        if dct[ch] > len(arr) / 4:
            return ch

    return 0


print(findSpecialInteger(findSpecialInteger, arr = [1,2,2,6,6,6,6,7,10]))


