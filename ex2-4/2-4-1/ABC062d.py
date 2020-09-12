
#########################自作実装#########################
import heapq 
N=int(input())
A=list(map(int, input().split()))
A_rev = [-x for x in A[::-1]]#逆順にして各要素を-1倍する
ans=-float("inf")
for k in range(N, 2*N+1):
	left=A[:k]
	right=A_rev[:(3*N-k)]

	heapq.heapify(left)
	heapq.heapify(right)

	for _ in range(k-N):
		heapq.heappop(left)
	for _ in range(2*N-k):
		heapq.heappop(right)

	ans= max(sum(left)+sum(right), ans)
print(ans)



#########################ABC解説実装#########################
#http://prdc.hatenablog.com/entry/2017/09/14/142721
import heapq
N=int(input())
A=list(map(int, input().split()))

left, right = A[:N], [-1 * i for i in A[2*N:]]
sum_left, sum_right = sum(left), sum(right)

results = [0] * (N+1)
results[0] = sum_left
results[N] = sum_right

heapq.heapify(left)
heapq.heapify(right)

for i in range(N, 2*N):
    v = A[i]
    p = heapq.heappushpop(left, v)
    sum_left += v - p
    results[i-N+1] += sum_left
    
for i in range(2*N-1, N-1, -1):
    v = -1 * A[i]
    p = heapq.heappushpop(right, v)
    sum_right += v - p
    results[i-N] += sum_right
print(max(results))
