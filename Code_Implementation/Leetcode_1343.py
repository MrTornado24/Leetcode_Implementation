from typing import List


def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
    res = [0]
    count = 0
    for i in range(len(arr)):
        res.append(res[-1] + arr[i])
    for i in range(len(res) - k):
        b = res[i+k]
        a = res[i]
        if b-a >= k * threshold:
            count += 1

    return count


print(numOfSubarrays(numOfSubarrays, [4,4,4,4], k = 4, threshold = 1))
