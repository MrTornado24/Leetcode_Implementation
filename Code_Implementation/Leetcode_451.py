from collections import Counter
from typing import List

import numpy as np


def frequencySort(self, s: str):
    # res = ''
    # counter = Counter(s)
    # while counter:
    #     max_ch = s[0]
    #     for ch in counter:
    #         if counter[ch] > counter[max_ch]:
    #             max_ch = ch
    #     res += max_ch * counter[max_ch]
    #     counter.pop(max_ch)
    # return res

    """
            :type s: str
            :rtype: str
            """
    n = len(s)
    sc = dict(Counter(s))
    ll = ['' for i in range(0, n+1)]
    isvisited = set()
    ret = ""
    for key, value in sc.items():
        ll[value] += key * value
    for i in range(n, -1, -1):
        if ll[i] != '':
            ret += ll[i]
    return ret


print(frequencySort(frequencySort, "Aabb"))


def twoSum(self, nums: List[int], target: int):
    if int(target / 2) in nums and Counter(nums)[int(target / 2)] > 1:
        print('hhhhh')
        return np.where(np.array(nums) == int(target / 2))[0][:2]

    for num in nums:
        if target - num in nums and target != 2 * num:
            return [nums.index(target - num), nums.index(num)]

    return []


print(twoSum(twoSum, [3,3], 6))

