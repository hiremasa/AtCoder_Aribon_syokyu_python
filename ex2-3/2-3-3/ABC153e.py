H, N = map(int, input().split())
A=[]
B=[]
for i in range(N):
	a,b = map(int, input().split())
	A.append(a)
	B.append(b)
#dp[i+1][h] := i番目の魔法まで見て、ライフをh以上削った時の最小魔力コスト
dp=[[float("inf")]*(H+1) for _ in range(N+1)]

for i in range(N):
	for h in range(H+1):
		if A[i]>=h:
			dp[i+1][h] = min(dp[i][h], B[i])
		else:
			dp[i+1][h] = min(dp[i][h], dp[i+1][h-A[i]]+B[i], dp[i][h-A[i]]+B[i])
print(dp[-1][-1])