# 给你一个整数数组 digits，你可以通过按任意顺序连接其中某些数字来形成 3 的倍数，请你返回所能得到的最大的 3 的倍数。
#
# 由于答案可能不在整数数据类型范围内，请以字符串形式返回答案。
#
# 如果无法得到答案，请返回一个空字符串。
from typing import List

import numpy as np


def largestMultipleOfThree(self, digits: List[int]) -> str:
    # 数学
    # 记录每个数字出现的频数
    # 如果数字和除3余1，则删除最小的除3余1的数字，若无，则删除两个最小的除3余2的数字
    # 当数字和除3余2时，方法类似
    # def delete(m):
    #     for i in range(m, 10, 3):
    #         if numDigits[i]:
    #             numDigits[i] -= 1
    #             return 1
    #     return 0
    #
    # numDigits = [0] * 10
    # s = 0
    # for d in digits:
    #     numDigits[d] += 1
    #     s += d
    # if s % 3 != 0:
    #     if delete(s % 3) == 0:
    #         delete(3 - s % 3)
    #         delete(3 - s % 3)
    # ans = ''
    # for d in range(9, -1, -1):
    #     ans += str(d) * numDigits[d]
    # return ans if ans == '' or ans[0] != '0' else '0'


    # 动态规划


print(largestMultipleOfThree(largestMultipleOfThree, digits = [8,1,9]))