from typing import List


def threeSum(nums: List[int], target: int):
    if len(nums) < 3 or not nums:
        return []
    res = []
    # nums = sorted(nums)
    for k in range(len(nums) - 2):
        if k > 0 and nums[k] == nums[k-1]: continue
        i, j = k + 1, len(nums) - 1

        while i < j:
            s = nums[i] + nums[j] + nums[k]
            if s < target:
                i += 1
                while i < j and nums[i] == nums[i-1]: i += 1
            elif s > target:
                j -= 1
                while i < j and nums[j] == nums[j+1]: j -= 1
            else:
                res.append([nums[k], nums[i], nums[j]])
                i += 1
                j -= 1
                while i < j and nums[j] == nums[j+1]: j -= 1
                while i < j and nums[i] == nums[i-1]: i += 1
    return res


def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    if len(nums) < 4 or not nums: return []
    ans = []
    res = []
    nums = sorted(nums)
    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i-1]: continue
        res = threeSum(nums[i+1:], target-nums[i])

        if res:
            for j in range(len(res)):
                res[j].append(nums[i])
                ans.append(res[j])
    return ans


print(fourSum(fourSum, [1,-2,-5,-4,-3,3,3,5], -11))



