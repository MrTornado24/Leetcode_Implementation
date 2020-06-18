# 求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。


def sumNums(n: int) -> int:
    # 一行 双百解法
    # return sum(range(n+1))

    # 递归
    return n > 0 and (n + sumNums(n-1))


print(sumNums(n=1))
