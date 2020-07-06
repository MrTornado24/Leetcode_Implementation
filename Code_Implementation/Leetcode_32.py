def longestValidParentheses(self, s: str) -> int:
    # 动态规划
    # 状态量为以字符串中某个字符为结束的最长有效括号个数
    # 状态转移：1. 如果字符为'（'，dp[i] = 0; 2. 如果字符为'）'， 则需判断前一个字符
    s = list(s)
    dp = [0] * len(s)

    for i in range(1, len(s)):
        if s[i] == '(':
            dp[i] = 0
        else:
            if s[i-1] == '(':
                dp[i] = dp[i-2]+2

            elif s[i-dp[i-1]-1] == '(' and i - dp[i-1] > 0:
                dp[i] = dp[i-dp[i-1]-2]+dp[i-1]+2

    return max(dp)


    # 栈
    s = list(s)
    res = [-1]
    ans = 0
    for i in range(len(s)):
        if s[i] == '(':
            res.append(i)
        else:
            res.pop()
            if res:
                ans = max(ans, i - res[0])
            else:
                res.append(i)
    return ans


print(longestValidParentheses(longestValidParentheses, "()()(())))(())"))



a = [1,2,3]
b = [1,2,4]
print(a-b)

