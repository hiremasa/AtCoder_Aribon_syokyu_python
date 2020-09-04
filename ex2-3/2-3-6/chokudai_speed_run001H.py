N=int(input())
seq=list(map(int, input().split()))

from bisect import bisect_left

dp=[float("inf")]*N

for i in range(N):
	dp[bisect_left(dp, seq[i])]=seq[i]
print(bisect_left(dp, float("inf")))
