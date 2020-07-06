# 在计算机界中，我们总是追求用有限的资源获取最大的收益。
#
# 现在，假设你分别支配着 m 个 0 和 n 个 1。另外，还有一个仅包含 0 和 1 字符串的数组。
#
# 你的任务是使用给定的 m 个 0 和 n 个 1 ，找到能拼出存在于数组中的字符串的最大数量。每个 0 和 1 至多被使用一次。
from typing import List


def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
    # 背包问题，动态规划
    dp = [[0] * (n+1) for _ in range(m+1)]
    for s in strs:
        ones = s.count('1')
        zeros = s.count('0')
        for i in range(m, zeros-1, -1):
            for j in range(n, ones-1, -1):
                dp[i][j] = max(dp[i][j], 1+dp[i-zeros][j-ones])

    return dp[-1][-1]


print(findMaxForm(findMaxForm, ["10", "0", "1"], m = 1, n = 1))