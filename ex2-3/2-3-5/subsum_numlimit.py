###############自作###############
N=int(input())
A=[]
M=[]
for i in range(N):
	a, m = map(int, input().split())
	A.append(a)
	M.append(m)
K=int(input())

dp=[[False]*(K+1) for _ in range(N+1)]
dp[0][0]=True

for i in range(N):
	for j in range(K+1):
		if j<A[i]:
			dp[i+1][j] = dp[i][j]
		else:
			k=0
			while 0<=k and k<=M[i] and k*A[i]<=j:
				dp[i+1][j] |=  dp[i][j-k*A[i]]
				k+=1
				if dp[i+1][j]:
					break
print("Yes" if dp[N][K] else "No")



###############蟻本###############
for i in range(N):
	for j in range(K+1):
		k=0
		while 0<=k and k<=M[i] and k*A[i]<=j:
			dp[i+1][j] |=  dp[i][j-k*A[i]]
			k+=1
			if dp[i+1][j]:
				break
print("Yes" if dp[N][K] else "No")