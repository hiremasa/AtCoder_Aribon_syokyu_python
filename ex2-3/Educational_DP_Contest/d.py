N, W = map(int, input().split())
weight, value = [0]*N, [0]*N
for i in range(N):
	weight[i], value[i] = map(int, input().split())


dp=[[0]*(W+1) for _ in range(N+1)]
#初期条件
#dp[0]=0
for i in range(N):
	for w in range(W+1):
		if w>=weight[i]:
			dp[i+1][w] = max(dp[i][w-weight[i]]+value[i], dp[i][w])
		else:
			dp[i+1][w]=dp[i][w]
print(dp[-1][-1])


#########################################################
import numpy as np
N, W = map(int, input().split())

dp=np.zeros((N+1, W+1), dtype=np.int64)

for i in range(1,N+1):
    w, v =list(map(int, input().split()))
    dp[i]=dp[i-1]
    dp[i][w:]=np.maximum(dp[i-1][:W-w+1]+v, dp[i-1][w:])
print(np.max(dp))

