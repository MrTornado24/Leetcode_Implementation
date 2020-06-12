# 给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
from typing import List


def findDuplicate(self, nums: List[int]) -> int:
    dct = {}
    for i, ch in enumerate(nums):
        if ch not in dct:
            dct[ch] = 1
        else:
            dct[ch] += 1
        if dct[ch] > 1:
            return ch


print(findDuplicate(findDuplicate, [1,3,4,2,2]))


