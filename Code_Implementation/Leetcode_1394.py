# 在整数数组中，如果一个整数的出现频次和它的数值大小相等，我们就称这个整数为「幸运数」。
#
# 给你一个整数数组 arr，请你从中找出并返回一个幸运数。
#
# 如果数组中存在多个幸运数，只需返回 最大 的那个。
# 如果数组中不含幸运数，则返回 -1 。
from typing import List


def findLucky(self, arr: List[int]) -> int:
    # 字典查找
    # dct = {}
    # res = []
    # for i, ch in enumerate(arr):
    #     if ch not in dct:
    #         dct[ch] = 1
    #     else:
    #         dct[ch] += 1
    # for ch in dct:
    #     if dct[ch] == ch:
    #         res.append(ch)
    # return max(res) if res else -1

    # 哈希表查找
    m = dict()
    for ch in arr:
        m[ch] = m.get(ch, 0) + 1
    ans = -1
    for (key, value) in m.items():
        if key == value:
            ans = max(ans, key)
    return ans


print(findLucky(findLucky, arr = [2,2,2,3,3]))
