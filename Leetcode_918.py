from typing import List


def max_withoutOVer(A):
    max1 = A[0]
    res = [0]
    for i in range(len(A)):
        res.append(res[-1]+A[i])
    j = 0
    for i in range(len(res)):
        if max1 < res[i]-res[j]:
            max1 = res[i]-res[j]
        if res[j+1] < res[j]:
            j += 1
    return max(max1, max(A))


def maxSubarraySumCircular(self, A: List[int]) -> int:
    # 暴力解法，复杂度为O(n^2)
    # maxS = []
    # max1 = max_withoutOVer(A)
    # for i in range(len(A)):
    #     if A[i] < 0:
    #         B = A[i:] + A[:i]
    #         maxS.append(max_withoutOVer(B))
    # return max(max1, max(maxS))

    # Kadane + 邻接数组
    ans, curr = A[0], A[0]
    for i, n in enumerate(A):
        if i == 0:
            ans = curr = n
        else:
            curr = n + max(curr, 0)
            ans = max(ans, curr)
    rightsums = [1] * len(A)
    rightsums[-1] = A[-1]
    print(ans)

    for i in range(len(A)-2, -1, -1):
        rightsums[i] = rightsums[i+1] + A[i]

    maxright = [1] * len(A)
    maxright[-1] = rightsums[-1]

    for i in range(len(A)-2, -1, -1):
        maxright[i] = max(maxright[i+1], rightsums[i])

    leftsums = 0
    for i in range(len(A)-2):
        leftsums += A[i]
        ans = max(ans, leftsums + maxright[i+2])
    return ans


print(maxSubarraySumCircular(maxSubarraySumCircular, [3,1,3,2,6]))
