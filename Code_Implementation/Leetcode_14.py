# 编写一个函数来查找字符串数组中的最长公共前缀。
from typing import List


def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ""
    min_len = min(len(x) for x in strs)
    ans = []
    for i in range(min_len):
        for j in range(len(strs)):
            if strs[0][i] != strs[j][i]:
                return ''.join(ans) if ans else ''
        ans.append(strs[0][i])

    return ''.join(ans) if ans else ''


print(longestCommonPrefix(longestCommonPrefix, ["aca","cba"]))

