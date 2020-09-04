from bisect import bisect_left

N=int(input())
box=[list(map(int, input().split())) for _ in range(N)]
dp=[float("inf")]*N
# h_i は昇順にした上で、h_i が等しい場合 w_i は降順にソートする
for w, h in sorted(box, key=lambda x: (x[0], -x[1])):
	dp[bisect_left(dp, h)]=h
print(bisect_left(dp, float("inf")))
