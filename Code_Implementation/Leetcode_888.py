# 爱丽丝和鲍勃有不同大小的糖果棒：A[i] 是爱丽丝拥有的第 i 块糖的大小，B[j] 是鲍勃拥有的第 j 块糖的大小。
#
# 因为他们是朋友，所以他们想交换一个糖果棒，这样交换后，他们都有相同的糖果总量。（一个人拥有的糖果总量是他们拥有的糖果棒大小的总和。）
#
# 返回一个整数数组 ans，其中 ans[0] 是爱丽丝必须交换的糖果棒的大小，ans[1] 是 Bob 必须交换的糖果棒的大小。
#
# 如果有多个答案，你可以返回其中任何一个。保证答案存在。
from typing import List


def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
    dctA, dctB = {}, {}
    for i, n in enumerate(A):
        if n not in dctA:
            dctA[n] = i
    for i, n in enumerate(B):
        if n not in dctB:
            dctB[n] = i

    diff = sum(B) - sum(A)
    for i in range(len(A)):

        if A[i] + diff/2 in dctB:
            return [A[i], A[i] + int(diff/2)]
    return []


print(fairCandySwap(fairCandySwap, A = [1,2,5], B = [2,4]))