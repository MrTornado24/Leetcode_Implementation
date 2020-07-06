from typing import List


# def threeSum(nums: List[int], target: int):
#     if len(nums) < 3 or not nums:
# return []
#     res = []
#     # nums = sorted(nums)
#     for k in range(len(nums) - 2):
#         if k > 0 and nums[k] == nums[k-1]: continue
#         i, j = k + 1, len(nums) - 1
#
#         while i < j:
#             s = nums[i] + nums[j] + nums[k]
#             if s < target:
#                 i += 1
#                 while i < j and nums[i] == nums[i-1]: i += 1
#             elif s > target:
#                 j -= 1
#                 while i < j and nums[j] == nums[j+1]: j -= 1
#             else:
#                 res.append([nums[k], nums[i], nums[j]])
#                 i += 1
#                 j -= 1
#                 while i < j and nums[j] == nums[j+1]: j -= 1
#                 while i < j and nums[i] == nums[i-1]: i += 1
#     return res
#
#
# def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#     if len(nums) < 4 or not nums: return []
#     ans = []
#     res = []
#     nums = sorted(nums)
#     for i in range(len(nums) - 3):
#         if i > 0 and nums[i] == nums[i-1]: continue
#         res = threeSum(nums[i+1:], target-nums[i])
#
#         if res:
#             for j in range(len(res)):
#                 res[j].append(nums[i])
#                 ans.append(res[j])
#     return ans

# def twoSum(nums, target, l, r):
#     dct = {}
#     n = nums[l:r+1]
#     if len(n) < 2:
#         return []
#     start = nums[l-1]
#     res = []
#     for i in range(l, r+1):
#         if target - nums[i]:
#             res.append([start, nums[i], target - nums[i]])
#         dct[nums[i]] = i
#     return res
#
#
# def threeSum(nums, target, l, r):
#     n = nums[l:r+1]
#     if len(n) < 3:
#         return []
#     start = nums[l-1]
#     res = []
#     for i in range(l, r+1):
#         if target <= 0 < nums[i]:
#             return []
#         if i > 1 and nums[i] == nums[i-1]:
#             continue
#         ll = twoSum(nums, target-nums[i], i+1, r)
#         if ll:
#             for l in ll:
#                 l.insert(0, start)
#                 res.append(l)
#     return res
#
#
# def fourSum(nums: List, target):
#     if len(nums) < 4:
#         return []
#     nums.sort()
#     res = set()
#     for i in range(len(nums)):
#         ll = threeSum(nums, target-nums[i], i+1, len(nums)-1)
#         if ll:
#             for l in ll:
#                 res.add(tuple(l))
#     return list(res)
#
#
#


def twoSum(nums, target, l, r):
    """
    :param r:
    :param l:
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    n = len(nums[l: r+1])
    if n < 2:
        return []

    start = nums[l - 1]
    dict1 = dict()
    ret = []
    for i in range(l, r+1):
        other = target - nums[i]
        if other in dict1:
            ret.append([start, other, nums[i]])
        dict1[nums[i]] = i

    return ret


# nums[l...r] 中返回 a+b+c=target
def threeSum(nums, target, l, r):
    """
    :param r:
    :param l:
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    n = len(nums[l : r+1])
    if n < 3:
        return list()

    start = nums[l-1]
    ret = list()
    for i in range(l, r+1):
        if nums[i] > 0 and target <= 0:
            break
        if i >= l+1 and nums[i] == nums[i-1]:
            continue
        ll = twoSum(nums, target-nums[i], i+1, r)
        if not ll:
            continue
        print(ll)
        print(ll[0])
        for i in range(len(ll)):
            list(ll[i]).insert(0, start)
            ret.append(i)
    return ret


def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    n = len(nums)
    if n < 4:
        return []
    nums.sort()
    ret = set()
    for i in range(n):
        ll = threeSum(nums, target-nums[i], i+1, n-1)
        if ll == list():
            continue
        for l in ll:
            ret.add(list(l))
    return list(ret)


print(fourSum(nums = [1, 0, -1, 0, -2, 2], target=0))


list = ['aaaa', 'bbbb']
print(len(list))