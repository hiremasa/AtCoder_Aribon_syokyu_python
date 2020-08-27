N, K=map(int, input().split())
h=list(map(int, input().split()))

dp=[float("inf")]*N
dp[0]=0

for i in range(1, N):
	if i==1:
		dp[i]=min(dp[i], abs(h[i]-h[i-1]))
	else:
		start=max(0, i-K)
		dp[i]=min(dp[j]+abs(h[j]-h[i]) for j in range(start, i))

print(dp[-1])