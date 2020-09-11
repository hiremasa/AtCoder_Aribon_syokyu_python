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



###############蟻本 O(n sigma k)###############
for i in range(N):
	for j in range(K+1):
		k=0
		while 0<=k and k<=M[i] and k*A[i]<=j:
			dp[i+1][j] |=  dp[i][j-k*A[i]]
			k+=1
			if dp[i+1][j]:
				break
print("Yes" if dp[N][K] else "No")


###############蟻本 O(nK)###############
#dp[i+1][j] := i番目まででjを作る際に余る最大のi番目の個数(作れない場合は-1)
dp=[[-1]*(K+1) for _ in range(N+1)]
dp[0][0]=0

for i in range(N):
	for j in range(1+K):
		if dp[j]>=0:
			dp[j]=M[i]
		elif j<A[i] or dp[j-a[i]]<=0:
			dp[j]=dp[j-a[i]]-1
		else:
			dp[j]=dp[j-a[i]]-1
if dp[N][K]>=0:
	print("Yes")
else:
	print("No")








