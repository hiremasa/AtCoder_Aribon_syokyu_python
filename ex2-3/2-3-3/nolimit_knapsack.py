########################O(nW^2)########################
N=int(input())
w=[]
v=[]
for i in range(N):
	a, b = map(int, input().split())
	w.append(a)
	v.append(v)
W=int(input())

dp=[[0]*(W+1) for _ in range(N+1)]

for i in range(N):
	for j in range(W+1):
		k=0
		while j>=w[i]*k:
			dp[i+1][j] = max(dp[i][j-k*w[i]]+k*v[i], dp[i+1][j])
			k+=1
print(dp[N][W])

########################O(nW)########################
dp=[[0]*(W+1) for _ in range(N+1)]
for i in range(N):
	for j in range(W+1):
		if j<w[i]:
			dp[i+1][j]=dp[i][j]
		else:
			dp[i+1][j]=max(dp[i][j], dp[i+1][j-w[i]+v[i]])
print(dp[N][W])