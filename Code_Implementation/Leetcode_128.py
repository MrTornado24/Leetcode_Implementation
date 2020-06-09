from typing import List


def longestConsecutive(self, nums: List[int]) -> int:
    if not nums:
        return 0
    res = [1]
    total = 1
    curr = 1
    j = 0
    nums.sort()
    print(nums)
    for i in range(1, len(nums)):
        res.append(nums[i] - nums[i-1])
    print(res)
    for i in range(1, len(res)):
        if res[i] == 0:
            continue
        elif res[i] == 1:
            if res[j] == 1:
                curr += 1
            else:
                curr = 2
            j = i
        else:
            curr = 1
            j = i
        total = max(total, curr)

    return total


print(longestConsecutive(longestConsecutive, [9,1,4,7,3,-1,0,5,8,-1,6]))
