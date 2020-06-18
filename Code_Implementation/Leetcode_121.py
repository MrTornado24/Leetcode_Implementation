# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
#
# 注意：你不能在买入股票前卖出股票。
from typing import List
import numpy as np


def maxProfit(self, prices: List[int]) -> int:
    if not prices:
        return 0
    min_price = prices[0]
    j = 0
    max_pro = 0
    for i in range(1, len(prices)):
        min_price = min(min_price, prices[j])
        max_pro = max(max_pro, prices[i] - min_price)
        j += 1
    return max_pro


print(maxProfit(maxProfit, [3,3,5,0,0,3,1,4]))

