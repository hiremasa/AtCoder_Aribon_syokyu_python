
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



################################################
import numpy as np
N, K = map(int, input().split())
H=np.array(list(map(int, input().split())) + [0] * K, dtype=np.int64)

dp=np.full(N+K, 1e+14, dtype=np.int64)
dp[0]=0
for i in range(1, N):
  dp[i:i + K]=np.minimum(dp[i:i + K], np.abs(H[i:i + K]-H[i-1])+dp[i-1])

print(dp[N - 1])  # 0-indexedに変換しておく



