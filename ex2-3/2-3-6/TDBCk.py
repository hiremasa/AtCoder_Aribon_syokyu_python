from bisect import bisect_left
from operator import itemgetter

N=int(input())
C=list(map(int, input().split()) for _ in range(N))


xlr = []
for i in C:
    xlr.append((i[0] - i[1], i[0] + i[1]))


# 条件を満たすために左端は降順にソートする
# 境界が重ならないように右端も降順にソートしておく
xlr = sorted(xlr, key=itemgetter(1), reverse=True)  # 右端
xlr = sorted(xlr, key=itemgetter(0), reverse=True)  # 左端

# 右端も条件を満たすように LIS を求める

dp = [float("inf")] * N

for i in range(N):
    dp[bisect_left(dp, xlr[i][1])] = xlr[i][1]

print(bisect_left(dp, float("inf")))