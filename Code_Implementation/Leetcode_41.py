# 给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
from typing import List


def firstMissingPositive(self, nums: List[int]) -> int:
    if not nums:
        return 1
    nums.sort()
    if nums[0] > 1 or nums[-1] < 1:
        return 1
    for i in range(1, nums[-1]):
        if i in nums:
            continue
        else:
            return i

    return nums[-1] + 1


print(firstMissingPositive(firstMissingPositive, [7,8,9,11,12]))