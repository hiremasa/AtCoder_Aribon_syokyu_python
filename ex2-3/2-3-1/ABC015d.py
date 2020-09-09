import numpy as np
W = int(input())
N, K = map(int, input().split())
dp=np.zeros((K+1, W+1), dtype=np.int64)

for i in range(N):
	w, v = map(int, input().split())
	dp[1:, w:] = np.maximum(dp[1:, w:], dp[:-1, :-w] + v)
	#右辺: 前者は使わなかった時, 後者は使った時
print(dp[-1, -1])