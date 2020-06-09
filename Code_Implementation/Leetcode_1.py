# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/two-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]
    #             break

    # sort = sorted(range(len(nums)), key=lambda k: nums[k])
    # head, tail = 0, len(nums)-1
    # sum = nums[sort[head]] + nums[sort[tail]]
    # while sum != target:
    #     if sum > target:
    #         tail -= 1
    #     elif sum < target:
    #         head += 1
    #     sum = nums[sort[head]] + nums[sort[tail]]
    # return [sort[head], sort[tail]]

    # 不能先补全字典后检索，为了避免target = n + n
    dct = {}
    for i, n in enumerate(nums):
        dct[n] = i

    for i, n in enumerate(nums):
        if target-n in dct and dct[target - n] != i:
            return [i, dct[target-n]]


print(twoSum(twoSum, nums=[3, 2, 4], target=6))
