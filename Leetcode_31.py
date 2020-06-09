from typing import List


def switch(i, j, nums):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


def nextPermutation(self, nums: List[int]) -> None:
    min = 0
    count = 0
    for i in range(len(nums)):
        if len(nums)-i-1 > 0 and nums[len(nums)-i-2] < nums[len(nums)-i-1]:
            count += 1
            min = len(nums) - 1
            for j in range(len(nums)-i-1, len(nums)):
                if nums[2*len(nums)-j-i-2] > nums[len(nums)-i-2]:
                    min = 2*len(nums)-j-i-2
                    break
            print(min)
            switch(len(nums)-i-2, min, nums)
            print(len(nums)-i-1)
            print(nums)
            k = len(nums) - 1
            while len(nums)-i-1 < k:
                switch(len(nums)-i-1, k, nums)
                i -= 1
                k -= 1

            break
    if count == 0:
        nums.sort()

    print(nums)


nextPermutation(nextPermutation, [2,2,7,5,4,3,2,2,1])
