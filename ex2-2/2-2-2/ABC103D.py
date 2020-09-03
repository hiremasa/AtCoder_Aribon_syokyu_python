from operator import itemgetter

N,M=map(int, input().split())

W=sorted([map(int, input().split()) for _ in range(N)], key=itemgetter(1))

removed=-1
ans=0

for s, e in W:
	if s>removed:
		removed=e-1
		ans+=1

print(ans)