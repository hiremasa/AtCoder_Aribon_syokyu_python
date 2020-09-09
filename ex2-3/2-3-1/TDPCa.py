N=int(input())
P=list(map(int, input().split()))
se=set([0])

for p in P:
	se |= set(x+p for x in se)
print(len(se))