from typing import List


def removeDuplicates(self, nums: List[int]):
    # i = 0
    # curr = 1
    # while i < len(nums):
    #     if i > 0 and nums[i] != nums[i-1]:
    #         nums[curr] = nums[i]
    #         curr += 1
    #     i += 1
    # return nums

    # 双指针
    if len(nums) == 0:
        return 0
    curr = 0
    for j in range(len(nums)):
        if nums[curr] != nums[j]:
            nums[curr+1] = nums[j]
            curr += 1
    print(nums[:curr+1])
    return curr+1


print(removeDuplicates(removeDuplicates, [1, 1, 2]))
