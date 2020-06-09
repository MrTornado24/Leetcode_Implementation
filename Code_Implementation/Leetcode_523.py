from typing import List


def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    # hashmap = {}
    # sums = 0
    #
    # hashmap[0] = 0
    # for i in range(len(nums)):
    #     sums += nums[i]
    #
    #     if k != 0:
    #         sums = sums % k
    #
    #     if sums in hashmap:
    #         if i-hashmap[sums] > 1:
    #             return True
    #     else:
    #         hashmap[sums] = i
    # return False

    dct = {0: 0}
    res = [0]
    for i in range(len(nums)):
        res.append(res[-1]+nums[i])
        mod = res[i+1] % k if k != 0 else res[i+1]
        if mod in dct:
            if i-dct[mod] > 0:
                return True
        else:
            dct[mod] = i+1
    return False


print(checkSubarraySum(checkSubarraySum, [4, 5], k=9))
