H,W = map(int,input().split())
Sx,Sy= map(int,input().split())
Gx,Gy= map(int,input().split())
P=list([int(i) for i in input().split()] for _ in range(H))

par = [-1] * (H*W)
edge = []
for h in range(H):
	for w in range(W-1):
		#cost, start, end
		edge.append([P[h][w]*P[h][w+1], h*W+w, h*W+(w+1)])
for h in range(H-1):
	for w in range(W):
		edge.append([P[h][w]*P[h+1][w], h*W+w, (h+1)*W+w])

ans = sum([sum(l) for l in P])


class Uf:
	def __init__(self, N):
		self.p = list(range(N))
		self.rank = [0] * N
		self.size = [1] * N
	#検索 ノード番号を受け取って一番上の親ノードの番号を帰す
	def root(self, x):
		if self.p[x] != x:
			self.p[x] = self.root(self.p[x])

		return self.p[x]
	#同じ集合に属するか判定
	def same(self, x, y):
		return self.root(x) == self.root(y)
	#併合
	def unite(self, x, y):
		# 根を探す
		u = self.root(x)
		v = self.root(y)

		if u == v: return

		#木の高さを比較し、低いほうから高いほうに辺を張る
		if self.rank[u] < self.rank[v]:
			self.p[u] = v
			self.size[v] += self.size[u]
			self.size[u] = 0
		else:
			self.p[v] = u
			self.size[u] += self.size[v]
			self.size[v] = 0
			#木の高さが同じなら片方を1増やす
			if self.rank[u] == self.rank[v]:
				self.rank[u] += 1
	#ノード番号を受け取って、そのノードが含まれている集合のサイズを返す
	def count(self, x):
		return self.size[self.root(x)]

#kruskal
uf=Uf(H*W)
cost = 0
edge.sort(reverse=True)

for c, u, v in edge:
	if not uf.same(u, v):
		cost+=c
		uf.unite(u, v)
ans+=cost
print(ans)