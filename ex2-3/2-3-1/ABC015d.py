import numpy as np
W = int(input())
N, K = map(int, input().split())
dp=np.zeros((K+1, W+1), dtype=np.int64)

for i in range(N):
	w, v = map(int, input().split())
	dp[1:, w:] = np.maximum(dp[1:, w:], dp[:-1, :-w] + v)
	#右辺: 前者は使わなかった時, 後者は使った時
print(np.max(dp))


#愚直に書く
W = int(input())
N, K = map(int, input().split())
weight = []
value = []
for i in range(N):
    a, b = map(int, input().split())
    weight.append(a)
    value.append(b)
#dp[i+1][k][w]:=i番目までを見てk枚使用し、重さwになった時のsum(value)の最大値
dp=[[[0]*(W+1) for _ in range(K+1)] for _ in range((N+1))]
for i in range(N):
	for k in range(K+1):
		for w in range(W+1):
			#枚数的に選べないとき
			if k>=K:
				dp[i+1][k][w] = dp[i][k][w]
			#枚数的に選べるとき
			else:
				if w>=weight[i]:
					dp[i+1][k][w] = max(dp[i][k-1][w-weight[i]]+value[i], dp[i][k][w])
				else:
					dp[i+1][k][w] = dp[i][k][w]

ans = 0
for i in range(K + 1):
    ans = max(ans, dp[N][i][W])
print(ans)