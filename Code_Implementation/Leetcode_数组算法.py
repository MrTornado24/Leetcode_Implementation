from typing import List


def moveZeroes(self, nums: List[int]) -> none:
    zeroPList = []  # 存放所有0元素的下标
    for i, num in enumerate(nums):
        if num == 0:
            zeroPList.append(i)
        elif len(zeroPList) != 0:
            index = zeroPList.pop(0)  # 取出数组中最靠前的0元素下标
            nums[i], nums[index] = nums[index], nums[i]  # 替换操作
            zeroPList.append(i)


print(moveZeroes(moveZeroes, [0,0,1]))
