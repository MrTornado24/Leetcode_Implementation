from typing import List


def threeSumClosest(self, nums: List[int], target: int) -> int:
    if len(nums) < 3 or not nums:
        return []
    res = []
    s = 0
    minDis = 88888888888
    minSum = 0
    nums = sorted(nums)
    for k in range(len(nums)-2):
        i, j = k + 1, len(nums) - 1
        while i < j:
            s = nums[i]+nums[j]+nums[k]
            if minDis > abs(s-target):
                minSum = s
            minDis = min(minDis, abs(target-s))
            if s - target < 0:
                i += 1
            elif s - target > 0:
                j -= 1
            else:
                return minSum
    return minSum


print(threeSumClosest(threeSumClosest, nums=[-1, 2, 1, -6, 2], target=3))


