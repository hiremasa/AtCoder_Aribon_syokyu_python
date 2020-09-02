import bisect

N=int(input())
c=list(int(input()) for _ in range(N))

dp=[float("inf")]*N

for i in range(N):
	dp[bisect.bisect_left(dp, c[i])]=c[i]

print(N-bisect.bisect_left(dp, float("inf")))