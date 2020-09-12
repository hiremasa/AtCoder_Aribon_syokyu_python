N=int(input())
L=list(map(int, input().split()))

import heapq
heapq.heapify(L)
ans=0

while len(L)>=2:
	min1 = heapq.heappop(L)
	min2 = heapq.heappop(L)
	temp=min1+min2
	ans+=temp
	heapq.heappush(L, temp)

print(ans)

