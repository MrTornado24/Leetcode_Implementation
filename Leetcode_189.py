# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
from typing import List


def switch(i, j, nums):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)
    temp = nums[len(nums)-k:]
    for i in reversed(range(len(nums)-k)):
        nums[i+k] = nums[i]
    for i in range(k):
        nums[i] = temp[i]
    print(nums)


rotate(rotate, [1,2,3,4,5,6,7], 3)
