# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。


def reverse(self, x: int) -> int:
    res = []
    ans = 0
    y = abs(x)
    while y > 0:
        res.append(y % 10)
        y = y // 10
    for i in range(len(res)):
        ans += res[i] * (10 ** (len(res) - i - 1))
    return ans if x > 0 else -ans


print(reverse(reverse, 120))
