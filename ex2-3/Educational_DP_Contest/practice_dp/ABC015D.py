W=int(input())
N, K = map(int, input().split())

weight = []
value = []
for i in range(N):
    a_, b_ = map(int, input().split())
    weight.append(a_)
    value.append(b_)


dp=[[[0]*(W+1) for _ in range(K+1)] for _ in range(N+1)]

#dp[i][k][w] := i 番目まで見て、k枚使用し、幅が合計wのときの最大値
for i in range(N):
	for k in range(K+1):
		for w in range(W+1):
			#これ以上貼れない
			if k==K:
				dp[i+1][k][w]=dp[i][k][w]
			else:
				if w>=weight[i]:
					dp[i+1][k][w]=max(dp[i][k-1][w-weight[i]]+value[i], dp[i][k][w])
				else:
					dp[i+1][k][w]=dp[i][k][w]

# 必ずk枚使う必要はない
ans = 0
for i in range(k + 1):
    ans = max(ans, dp[N][i][W])

print(ans)
