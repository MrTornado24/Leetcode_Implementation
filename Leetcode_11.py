from typing import List


def maxArea(self, height: List[int]) -> int:
    maxa = 0
    curr = 0
    head = 0
    tail = len(height) - 1
    while head < tail:
        curr = min(height[head], height[tail]) * (tail - head)
        maxa = max(curr, maxa)
        if height[head] > height[tail]:
            tail -= 1
        else:
            head += 1
    return maxa



print(maxArea(maxArea, [1,8,6,2,5,4,8,3,7]))
