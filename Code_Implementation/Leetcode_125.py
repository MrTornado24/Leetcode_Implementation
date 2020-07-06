# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。


def isPalindrome(self, s: str) -> bool:
    res = []
    if not s:
        return True
    s = s.lower()
    for i in range(len(s)):
        if s[i].isdigit() or s[i].isalpha():
            res.append(s[i])

    if not res or len(res) == 1:
        return True

    if len(res) % 2 == 1:
        i = len(res) // 2 - 1
        j = len(res) // 2 + 1
    else:
        if res[len(res)//2] != res[len(res)//2-1]:
            return False
        if len(res) == 2 and res[0] == res[1]:
            return True
        i = len(res) // 2 - 2
        j = len(res) // 2 + 1
    print(i, j)
    print(res[:i+1])
    print(res[:j-1:-1])
    if res[:i+1] == res[:j-1:-1]:
        return True
    else:
        return False


print(isPalindrome(isPalindrome, "A man, a plan, a canal: Panama"))




