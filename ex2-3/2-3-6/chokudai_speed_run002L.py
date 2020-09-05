N=int(input())

AB=[]
for i in range(N):
	a, b = map(int, input().split())
	if a<b:
		a, b  = b, a
	AB.append([a, b])

AB=sorted(AB, key=lambda x: (x[0], -x[1]))
from bisect import bisect_left
dp=[float("inf")]*N

for a, b in AB:
	dp[bisect_left(dp, b)]=b

print(bisect_left(dp, float("inf")))
