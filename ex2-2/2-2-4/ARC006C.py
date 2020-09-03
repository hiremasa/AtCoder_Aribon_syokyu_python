
N=int(input())
W=[int(input()) for _ in range(N)]


TOP=[float("inf")]
for w in W:
	flag=True

	for i in range(len(TOP)):
		if TOP[i]>=w:
			TOP[i]=w
			flag=False
			break
	if flag:
		TOP.append(w)

print(len(TOP))



#DP
import bisect
N=int(input())
dp=[float("inf")]*N

for i in range(N):
	w=int(input())
	dp[bisect.bisect_left(dp, w)]=w

print(bisect.bisect_left(dp, float("inf")))