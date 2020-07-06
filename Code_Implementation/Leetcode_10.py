# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。


def isMatch(self, s: str, p: str) -> bool:
    m, n = len(s), len(p)

    def match(i, j):
        if i == 0:
            return False
        if p[j-1] == '.':
            return True

        return p[j-1] == s[i-1]

    f = [[False] * (n+1) for _ in range(m+1)]
    f[0][0] = True
    for i in range(m+1):
        for j in range(1, n+1):
            if p[j-1] == '*':
                f[i][j] |= f[i][j-2]
                if match(i, j-1):
                    f[i][j] |= f[i-1][j]
            else:
                if match(i, j):
                    f[i][j] |= f[i-1][j-1]

    return f[m][n]


print(isMatch(isMatch, s = "aa", p = "a*"))



