# 给定两个字符串s1, s2，找到使两个字符串相等所需删除字符的ASCII值的最小和。
import numpy as np


def minimumDeleteSum(self, s1: str, s2: str) -> int:
    m = len(s1)
    n = len(s2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    dp[0][0] = 0
    cost = 0
    for i in range(m):
        dp[i+1][0] = dp[i][0] + ord(s1[i])
    for j in range(n):
        dp[0][j+1] = dp[0][j] + ord(s2[j])
    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j]
            else:
                dp[i+1][j+1] = min(dp[i][j+1] + ord(s1[i]), dp[i+1][j] + ord(s2[j]))
    return dp[-1][-1]


print(minimumDeleteSum(minimumDeleteSum, s1 = "delete", s2 = "leet"))
