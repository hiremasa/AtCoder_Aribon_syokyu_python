import heapq
N=int(input())
ans=0
xs=list(map(int, input().split()))
heapq.heapify(xs)

while len(xs)>1:
	x1_x2=heapq.heappop(xs)+heapq.heappop(xs)
	ans+=x1_x2
	heapq.heappush(xs, x1_x2)
print(ans)

