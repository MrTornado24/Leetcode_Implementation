# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
import functools


@functools.lru_cache(100)
def climbStairs(n: int) -> int:
    # 空间复杂度为O(n)的动态规划
    # dp = {1: 1, 2: 2}
    # for i in range(3, n+1):
    #     dp[i] = dp[i-1] + dp[i-2]
    # return dp[n]

    # 利用缓存装饰器加速的暴力递归
    # if n == 1:
    #     return 1
    # if n == 2:
    #     return 2
    # return climbStairs(n-1)+climbStairs(n-2)

    # 空间复杂度为O(1)的动态规划
    if n == 1:
        return 1
    if n == 2:
        return 2
    a, b, temp = 1, 2, 0
    for i in range(3, n+1):
        temp = a + b
        a = b
        b = temp
    return temp


print(climbStairs(3))
