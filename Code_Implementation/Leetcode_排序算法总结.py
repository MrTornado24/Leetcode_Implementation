# 冒泡排序
from typing import List


def bubbleSort(nums: List) -> List:
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


print(bubbleSort([2, 3, 1, 38, 13, 15, 17, 11, 9]))


def selectionSort(nums: List) -> List:
    for i in range(len(nums) - 1):
        min_val = nums[i]
        min_ind = i
        for j in range(i+1, len(nums)):
            if min_val > nums[j]:
                min_val = nums[j]
                min_ind = j

        nums[i], nums[min_ind] = nums[min_ind], nums[i]

    return nums


print(selectionSort([2, 3, 1, 38, 13, 15, 17, 11, 9]))


def insertionSort(nums: List) -> List:
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i
        while j >= 1 and temp < nums[j-1]:
            nums[j] = nums[j-1]
            j -= 1
        nums[j] = temp
    return nums


print(insertionSort([2, 3, 1, 38, 13, 15, 17, 11, 9]))


def shellSort(nums: List) -> List:
    k = len(nums) // 2
    while k > 0:
        for i in range(k, len(nums)):
            temp = nums[i]
            j = i
            while j >= k and temp < nums[int(j-k)]:
                nums[j] = nums[int(j-k)]
                j -= k
            nums[j] = temp
        k = k // 2
    return nums


print(shellSort([2, 3, 1, 38, 13, 15, 17, 11, 9]))


def mergeSort(nums: List) -> List:
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    return merge(mergeSort(left), mergeSort(right))


def merge(nums1: List, nums2: List) -> List:
    res = []
    m = len(nums1)
    n = len(nums2)
    i, j = 0, 0
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            res.append(nums1[i])
            i += 1
        else:
            res.append(nums2[j])
            j += 1
    if i == m:
        for k in range(j, n):
            res.append(nums2[k])
    elif j == n:
        for k in range(i, m):
            res.append(nums1[k])
    return res


print(mergeSort([2, 3, 1, 38, 13, 15, 17, 11, 9, 2, 100]))


def quickSort(nums: List) -> List:
    if len(nums) >= 2:
        mid = nums[len(nums) // 2]
        nums.remove(mid)
        right, left = [], []
        for num in nums:
            right.append(num) if num > mid else left.append(num)
        return quickSort(left) + [mid] + quickSort(right)
    else:
        return nums


print(quickSort([2, 3, 1, 38, 13, 15, 17, 11, 9, 2, 100]))















