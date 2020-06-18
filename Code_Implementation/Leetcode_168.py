def convertToTitle(self, n: int) -> str:

    # dct = {}
    # ans = []
    # res = []
    # for i in range(1, 27):
    #     dct[i] = chr(65+i-1)
    # while n > 0:
    #     if n == 26:
    #         res.append(26)
    #         break
    #     else:
    #         if n % 26 == 0:
    #             res.append(26)
    #             n = n - 26
    #         else:
    #             res.append(n % 26)
    #     n = n // 26
    # res.reverse()
    # print(res)
    # for i in range(len(res)):
    #     ans.append(dct[res[i]])
    # return "".join(ans)

    # 简化版：
    res = ""
    while n:
        n, y = divmod(n, 26)
        if y == 0:
            n -= 1
            y = 26
        res = chr(y+64) + res
    return res


print(convertToTitle(convertToTitle, 701))

