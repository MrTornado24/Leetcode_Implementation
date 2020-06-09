from typing import List


def checkPossibility(self, nums: List[int]) -> bool:
    count = 0
    if not nums or len(nums) == 1:
        return True
    count = 0
    for i in range(1, len(nums)):
        if count > 1:
            return False
        if nums[i] >= nums[i-1]:
            continue
        count += 1
        if i > 1 and nums[i-2] > nums[i]:
            nums[i] = nums[i-1]
        else:
            nums[i-1] = nums[i]
    return count <= 1


print(checkPossibility(checkPossibility, [4,2,3]))