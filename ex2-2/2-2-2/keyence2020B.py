N=int(input())
X=[]
for i in range(N):
	x, L = map(int, input().split())
	X.append([x-L, x+L])
from operator import itemgetter

W=sorted(X, key=itemgetter(1))

ans=0
last=-float("inf")

for s, e in W:
	if s>=last:
		last=e
		ans+=1
print(ans)