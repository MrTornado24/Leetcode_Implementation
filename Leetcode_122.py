# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
import numpy as np
from typing import List


def maxProfit(self, prices: List[int]) -> int:
    ans, sum = [], 0
    for i in range(len(prices)-1):
        ans.append(prices[i+1] - prices[i])

    for i in range(ans):
        if ans[i] > 0:
            sum += ans[i]
    return sum


X = ['dog', 'cat', 'cat', 'pig', 'dog']
dct = {}
max = 0
for ch in X:
    if ch not in dct:
        dct[ch] = 1
    else:
        dct[ch] += 1

dct = sorted(dct)
print(dct[0])

np.arr