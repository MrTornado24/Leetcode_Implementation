from typing import List

# 给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。
#
# 一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。
#
# 返回一对观光景点能取得的最高分。


def maxScoreSightseeingPair(self, A: List[int]) -> int:
    ans = 0
    mx = A[0] + 0
    for i in range(1, len(A)):
        ans = max(ans, mx + A[i] - i)
        mx = max(mx, A[i] + i)
    return ans


print(maxScoreSightseeingPair(maxScoreSightseeingPair, [6,3,7,4,7,6,6,4,9]))
