# 你有两个字符串，即pattern和value。 pattern字符串由字母"a"和"b"组成，用于描述字符串中的模式。
# 例如，字符串"catcatgocatgo"匹配模式"aabab"（其中"cat"是"a"，"go"是"b"），该字符串也匹配像"a"、"ab"和"b"这样的模式。
# 但需注意"a"和"b"不能同时表示相同的字符串。编写一个方法判断value字符串是否匹配pattern字符串。


def patternMatching(self, pattern: str, value: str) -> bool:
    count_a = pattern.count('a')
    count_b = pattern.count('b')
    if count_a < count_b:
        count_a, count_b = count_b, count_a
        pattern = ''.join('a' if ch == b else 'b' for ch in pattern)

    if not value:
        return count_b == 0
    if not pattern:
        return False
    for len_a in range(len(value) // count_a + 1):
        rest = len(value) - count_a * len_a
        if (count_b == 0 and rest == 0) or (count_b != 0 and rest % count_b == 0):
            pos = 0
            mode_a, mode_b, curr_a, curr_b = None, None, None, None
            len_b = 0 if count_b == 0 else rest // count_b
            for ch in pattern:
                if ch == 'a':
                    curr_a = value[pos:pos+len_a]
                    if not mode_a:
                        mode_a = curr_a
                    elif mode_a != curr_a:
                        break
                    pos += len_a
                else:
                    curr_b = value[pos:pos+len_b]
                    if not mode_b:
                        mode_b = curr_b
                    elif mode_b != curr_b:
                        break
                    pos += len_b

            if mode_a != mode_b:
                return True

    return False


print(patternMatching(patternMatching, pattern="abba", value="dogcatcatdog"))
