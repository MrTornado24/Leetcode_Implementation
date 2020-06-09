# 如果一个由 '0' 和 '1' 组成的字符串，是以一些 '0'（可能没有 '0'）后面跟着一些 '1'（也可能没有 '1'）的形式组成的，那么该字符串是单调递增的。
#
# 我们给出一个由字符 '0' 和 '1' 组成的字符串 S，我们可以将任何 '0' 翻转为 '1' 或者将 '1' 翻转为 '0'。
#
# 返回使 S 单调递增的最小翻转次数。


# 动态规划
# dp[i][0]可以由dp[i-1][0]或者dp[i-1][1]变化而来，用zero和one记录0和1的最少翻转次数
def minFlipsMonoIncr(self, S: str) -> int:
    # zero, one = 0, 0
    # for ch in S:
    #     if ch == '0':
    #         one = min(zero+1, one+1)
    #     else:
    #         one = min(zero, one)
    #         zero = zero + 1
    # return min(zero, one)


# 遍历列表找到一个分界点使得分界点之前（包含分界点）的1的个数与分界点之后0的个数之和最小
    m = S.count('0') # 开始时分界点在列表最前端
    res = [m]
    for ch in S:
        if ch == '1':
            m += 1
        else:
            m -= 1
        res.append(m)
    return min(res)
