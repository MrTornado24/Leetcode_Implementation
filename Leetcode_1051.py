from typing import List


def heightChecker(self, heights: List[int])->int:
    sort = sorted(heights)
    count = 0
    for i in range(len(heights)):
        if heights[i] != sort[i]:
            count += 1
    return count


print(heightChecker(heightChecker, [5,1,2,3,4]))