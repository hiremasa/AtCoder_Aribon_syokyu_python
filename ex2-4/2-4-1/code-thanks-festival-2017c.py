import heapq
N, K = map(int, input().split())

machine=[]
for i in range(N):
	a, b = map(int, input().split())
	heapq.heappush(machine, (a,b))

ans=0
for i in range(K):
	a, b = heapq.heappop(machine)
	ans+=a
	a+=b
	heapq.heappush(machine, (a, b))

print(ans)
