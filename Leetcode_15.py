
from typing import List


# def findSum_k(k, nums):
#     dct = {}
#     for i, n in enumerate(nums):
#         if k - n in dct:
#             return [dct[k-n], i]
#         dct[n] = i
#
#
# def threeSum(self, nums: List[int]):
#     res = []
#     if len(nums) < 3:
#         return []
#     for i in range(len(nums)):
#         if findSum_k(-nums[i], nums[0:i] + nums[i+1:]):
#             ans = findSum_k(-nums[i], nums[0:i] + nums[i+1:])
#             group = [nums[ans[0]], nums[ans[1]], nums[i]]
#             group = sorted(group)
#             if group not in res:
#                 res.append(group)
#     return list(res)





def threeSum(self, nums: List[int]):
    if len(nums) < 3 or not nums:
        return []
    nums = sorted(nums)
    res = []
    for k in range(len(nums) - 2):
        if nums[k] > 0: break
        if k > 0 and nums[k] == nums[k-1]: continue
        i, j = k + 1, len(nums) - 1
        while i < j:
            s = nums[k] + nums[i] + nums[j]
            if s > 0:
                j -= 1
                while i < j and nums[j] == nums[j+1]: j -= 1
            elif s < 0:
                i += 1
                while i < j and nums[i] == nums[i-1]: i += 1
            else:
                res.append([nums[k], nums[i], nums[j]])
                i += 1
                j -= 1
                while i < j and nums[j] == nums[j+1]: j -= 1
                while i < j and nums[i] == nums[i-1]: i += 1
    return res




print(threeSum(threeSum, [0,0,0,0]))
