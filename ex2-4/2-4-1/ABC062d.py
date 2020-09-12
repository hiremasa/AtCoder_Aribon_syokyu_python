import heapq 
N=int(input())
A=list(map(int, input().split()))
ans=-float("inf")
for k in range(N, 2*N+1):
	left=A[:k]
	right=[-i for i in A[k:]] #各要素を-1倍する

	heapq.heapify(left)
	heapq.heapify(right)

	for _ in range(k-N):
		heapq.heappop(left)
	for _ in range(2*N-k):
		heapq.heappop(right)

	ans= max(sum(left)+sum(right), ans)
print(ans)