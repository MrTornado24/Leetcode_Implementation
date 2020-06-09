# 给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，
# 其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
from typing import List


def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    L, R, ans = [0] * n, [0] * n, [0] * n
    L[0] = 1
    for i in range(1, n):
        L[i] = nums[i-1] * L[i-1]
    R[n-1] = 1
    for i in reversed(range(n-1)):
        R[i] = nums[i+1] * R[i+1]
    for i in range(n):
        ans[i] = L[i] * R[i]
    return ans


print(productExceptSelf(productExceptSelf, [1,2,3,4]))