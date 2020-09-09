N, M = map(int, input().split())
S = input()
T = input()
#dp[i+1][j]=s1..siとt1..tjに対するLCSの長さ
dp = [[0] * (M + 1) for i in range(N + 1)]

for i in range(N):
	for j in range(M):
		if S[i]==T[j]:
			dp[i+1][j+1]=dp[i][j] +1
		else:
			dp[i+1][j+1]=max(dp[i+1][j], dp[i][j+1])

print(dp[n][m])
