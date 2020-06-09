# 给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。
from typing import List


def subarraysDivByK(self, A: List[int], K: int) -> int:
    # 暴力解法
    # res = []
    # count = 0
    # for i in range(len(A)):
    #     if i == 0:
    #         res.append(A[i])
    #     else:
    #         res.append(res[-1]+A[i])
    # for i in range(len(res)):
    #     res[i] = res[i] % K
    #     if res[i] == K or res[i] == 0:
    #         count += 1
    # for i in range(len(res)):
    #     for j in range(i+1, len(res)):
    #         if res[i] == res[j]:
    #             count += 1
    # return count

    # 哈希表
    record = {0 : 1}
    count = 0
    total = 0
    for i in range(len(A)):
        total = total + A[i]
        mod = total % K
        same = record.get(mod, 0)
        count += same
        record[mod] = same + 1

    return count


print(subarraysDivByK(subarraysDivByK, A = [5], K = 9))