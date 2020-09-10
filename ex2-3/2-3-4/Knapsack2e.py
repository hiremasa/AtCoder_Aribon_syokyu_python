N, W = map(int, input().split())
w=[]
v=[]
for i in range(N):
	a, b = map(int, input().split())
	w.append(a)
	v.append(b)
#dp[i+1][j] := i番目までの品物から総和がjとなるように選んだ時の重さの総和の最小値
dp=[[float("inf")]*(max(v)*N+1) for _ in range(N+1)]
#初期条件
dp[0][0]=0
for i in range(N):
	for j in range(max(v)*N+1):
		if v[i]>j:
			dp[i+1][j] = dp[i][j]
		else:
			dp[i+1][j] = min(dp[i][j], dp[i][j-v[i]]+w[i])

ans=0
for j in range(max(v)*N+1):
	if dp[N][j]<=W:
		ans=j
print(ans)