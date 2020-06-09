# 这个问题和“最多能完成排序的块”相似，但给定数组中的元素可以重复，输入数组最大长度为2000，其中的元素最大为10**8。
#
# arr是一个可能包含重复元素的整数数组，我们将这个数组分割成几个“块”，并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。
#
# 我们最多能将数组分成多少块？
from typing import List
import numpy as np


def maxChunksToSorted(self, arr: List[int]) -> int:
    dp = [0] * len(arr)
    dp[0] = 1
    if len(arr) == 1:
        return 1

    for i in range(1, len(arr)):
        if min(arr[i:]) >= max(arr[:i]):
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i-1]
    return dp[-1]


print(maxChunksToSorted(maxChunksToSorted, arr = [5,1]))