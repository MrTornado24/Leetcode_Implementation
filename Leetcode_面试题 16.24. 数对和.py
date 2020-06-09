# 设计一个算法，找出数组中两数之和为指定值的所有整数对。一个数只能属于一个数对。
from typing import List


def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
    # 排序 + 双指针
    nums.sort()
    res = []
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] + nums[j] > target:
            j -= 1
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            res.append([nums[i], nums[j]])
            i += 1
            j -= 1
    return res


    # 哈希表
    h = dict()
    res = []
    for i in range(len(nums)):
        if h.get(target - nums[i], 0) == 0:
            h[nums[i]] = h.get(nums[i], 0) + 1
        else:
            res.append([nums[i], target - nums[i]])
            h[target - nums[i]] -= 1
    return res


print(pairSums(pairSums, nums = [], target = 11))