#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_12_A&lang=jp
import heapq
N=int(input())
next=[]#隣接管理のリスト
for _ in range(N):
	l = list(map(int, input().split()))
	next.append([(c, i) for i, c in enumerate(l) if c != -1])
visit=[0]*N
connection=0
q=[(0, 0)] #(cost, v)
heapq.heapify(q)
ans=0

while q:
	cost, v = heap.heappop(q)
	if visit[v]:
		continue

	#そのノードと繋げる
	visit[v]=1
	connection+=1
	ans+=cost
	#新たに繋げたノードから行けるところをエンキュー
	for i in next[i]:
		heapq.heappush(q, i)

	if connection==N:
		break
print(ans)

###############Scipy###############
import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix, coo_matrix, lil_matrix
N=int(input())
L=[]
for _ in range(N):
	l = list(map(int, input().split()))
	#[真の値 if 条件式 else 偽の値 for 任意の変数名 in 元のリスト]
	l=[w if w!=-1 else 0 for w in l]
	L.append(l)
#print(L)

csr = csr_matrix(L)
mst = minimum_spanning_tree(csr, True)

print(mst.sum())