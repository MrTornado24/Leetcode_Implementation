# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
from nltk import collections


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    ans = collections.defaultdict(list)
    for ch in strs:
        ans[tuple(sorted(ch))].append(ch)
    return ans.values()


