# 最初在一个记事本上只有一个字符 'A'。你每次可以对这个记事本进行两种操作：
#
# Copy All (复制全部) : 你可以复制这个记事本中的所有字符(部分的复制是不允许的)。
# Paste (粘贴) : 你可以粘贴你上一次复制的字符。
# 给定一个数字 n 。你需要使用最少的操作次数，在记事本中打印出恰好 n 个 'A'。输出能够打印出 n 个 'A' 的最少操作次数。


def minSteps(self, n: int) -> int:
    # 动态规划
    # def maxFactor(n):
    #     for i in range(n//2, 0, -1):
    #         if n % i == 0:
    #             return i
    # dp = [10**9] * (n+1)
    # dp[0], dp[1] = 0, 0
    # for i in range(2, n+1):
    #     if i % 2 == 0:
    #         dp[i] = dp[int(i/2)] + 2
    #     else:
    #         index = maxFactor(i)
    #         dp[i] = dp[index] + (i // index)
    # return dp[n]

    # 素数分解
    # 可以把所有操作分成一个个以copy为首的数组，数组长度之积为n，数组长度之和为总操作数。整体思想是让每个数组的长度均为素数，则使总操作数最小。
    d = 2
    ans = 0
    while n > 1:
        while n % d == 0:
            ans += d
            n = n // d
        d += 1
    return ans


print(minSteps(minSteps, 6))
