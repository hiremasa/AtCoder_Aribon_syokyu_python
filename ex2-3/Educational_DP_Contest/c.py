N=int(input())
abc=[list(map(int, input().split())) for _ in range(N)]

dp=[[0]*3 for i in range(N+1)]


for i in range(N):
	dp[i+1][0]=max(max(dp[i][1],dp[i][2])+abc[i][0],dp[i+1][0])
	dp[i+1][1]=max(max(dp[i][2],dp[i][0])+abc[i][1],dp[i+1][1])
	dp[i+1][2]=max(max(dp[i][0],dp[i][1])+abc[i][2],dp[i+1][2])
print(max(dp[-1]))
