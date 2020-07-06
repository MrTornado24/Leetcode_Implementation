# 给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。


def maxPoints(self, points: List[List[int]]) -> int:
    if not points:
        return 0
    if len(points) == 1:
        return 1
    res = 0
    dct = collections.defaultdict(list)
    dct1 = dict()
    for i in range(len(points)):
        if tuple(points[i]) in dct or tuple(points[i]) in dct1:
            continue
        for j in range(len(points)):
            if i == j:
                continue

            elif points[i][0] == points[j][0] and points[i][1] != points[j][1]:
                dct[tuple(points[i])].append('a')
            elif points[i] == points[j]:
                if tuple(points[i]) in dct1:
                    dct1[tuple(points[i])] += 1
                else:
                    dct1[tuple(points[i])] = 1
                continue
            else:
                dct[tuple(points[i])].append(Decimal(points[i][1]-points[j][1]) / Decimal(points[i][0]-points[j][0]))
    print(dct)
    print(dct1)
    if not dct:
        return 1+dct1[tuple(points[0])]
    for point in dct:
        dct2 = Counter(dct[point])
        res = max(res, max(dct2.values())+1+dct1.get(point, 0))
    return res