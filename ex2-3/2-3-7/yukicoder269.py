#https://yukicoder.me/problems/no/269
N, S, K = map(int, input().split())
M=S-K*N*(N-1)//2
#dp[i][j] :=jをi分割の総数
if M < 0:
    print(0)
else:
	dp=[[0]*(M+1) for _ in range(N+1)]
	dp[0][0]=1
	for i in range(N+1):
		for j in range(M+1):
			if j-i>=0:
				dp[i][j]=(dp[i-1][j]+dp[i][j-i])%(10**9+7)
			else:
				dp[i][j]=dp[i-1][j]
	print(dp[-1][-1])
