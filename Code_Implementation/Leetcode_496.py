# 给定两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
# nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。
from typing import List


def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    # 单调栈
    stack = []
    ans = [-1] * len(nums2)
    res = []
    for i in range(len(nums2)):
        while stack and nums2[i] > nums2[stack[-1]]:
            pre = stack.pop()
            ans[pre] = nums2[i]
        stack.append(i)
    for i in range(len(nums1)):
        res.append(ans[nums2.index(nums1[i])])
    return res


print(nextGreaterElement(nextGreaterElement, nums1 = [4,1,2], nums2 = [1,3,4,2]))