def isIsomorphic(self, s: str, t: str) -> bool:
    m = len(s)
    n = len(t)
    s, t = list(s), list(t)
    if m != n:
        return False
    dct = {}
    for i in range(len(s)):
        if s[i] not in dct:
            dct[s[i]] = t[i]
        else:
            if dct[s[i]] != t[i]:
                return False

    dct = {}
    for i in range(len(t)):
        if t[i] not in dct:
            dct[t[i]] = s[i]
        else:
            if dct[t[i]] != s[i]:
                return False

    return True


print(isIsomorphic(isIsomorphic, "aba", "baa"))

