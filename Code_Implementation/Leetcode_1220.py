# 给你一个整数 n，请你帮忙统计一下我们可以按下述规则形成多少个长度为 n 的字符串：
#
# 字符串中的每个字符都应当是小写元音字母（'a', 'e', 'i', 'o', 'u'）
# 每个元音 'a' 后面都只能跟着 'e'
# 每个元音 'e' 后面只能跟着 'a' 或者是 'i'
# 每个元音 'i' 后面 不能 再跟着另一个 'i'
# 每个元音 'o' 后面只能跟着 'i' 或者是 'u'
# 每个元音 'u' 后面只能跟着 'a'


def countVowelPermutation(self, n: int) -> int:
    dp_a = [0] * (n+1)
    dp_e = [0] * (n+1)
    dp_i = [0] * (n+1)
    dp_o = [0] * (n+1)
    dp_u = [0] * (n+1)
    dp_a[1] = 1
    dp_e[1] = 1
    dp_i[1] = 1
    dp_o[1] = 1
    dp_u[1] = 1
    for i in range(2, n + 1):
        dp_a[i] = dp_e[i-1] + dp_i[i-1] + dp_u[i-1]
        dp_e[i] = dp_a[i-1] + dp_i[i-1]
        dp_i[i] = dp_e[i-1] + dp_o[i-1]
        dp_o[i] = dp_i[i-1]
        dp_u[i] = dp_i[i-1] + dp_o[i-1]
    return dp_a[n] + dp_e[n] + dp_i[n] + dp_o[n] + dp_u[n]


print(countVowelPermutation(countVowelPermutation, 5))

