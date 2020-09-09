import numpy as np

N, W = map(int, input().split())
dp=np.zeros((N+1, W+1), dtype=np.int64)

for i in range(1, N+1):
	w, v =list(map(int, input().split()))
	dp[i]=dp[i-1]
	dp[i][w:]=np.maximum(dp[i-1][w:], dp[i-1][W-w+1])
print(np.max(dp))


dp = np.zeros(W + 1, np.int64)
for w, v in zip(W, V):
    np.maximum(dp[w:], dp[:-w] + v, out=dp[w:])
print(dp.max())