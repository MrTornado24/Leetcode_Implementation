# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
#
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
from typing import List


def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    # 首先找到newinterval开始的那个区间，输出
    # 输出newinterval，若有重叠，注意merge
    # 依次输出之后的区间，注意merge
    # init data
    new_start, new_end = newInterval
    idx, n = 0, len(intervals)
    output = []

    # add all intervals starting before newInterval
    while idx < n and new_start > intervals[idx][0]:
        output.append(intervals[idx])
        idx += 1

    # add newInterval
    # if there is no overlap, just add the interval
    if not output or output[-1][1] < new_start:
        output.append(newInterval)
    # if there is an overlap, merge with the last interval
    else:
        output[-1][1] = max(output[-1][1], new_end)

    # add next intervals, merge with newInterval if needed
    while idx < n:
        interval = intervals[idx]
        start, end = interval
        idx += 1
        # if there is no overlap, just add an interval
        if output[-1][1] < start:
            output.append(interval)
        # if there is an overlap, merge with the last interval
        else:
            output[-1][1] = max(output[-1][1], end)
    return output


print(insert(insert, intervals = [[1,5]], newInterval = [6,8]))
