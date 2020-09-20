#https://gist.github.com/lethe2211/cca597c45148c5e55c3f
N, M, T = map(int, input().split())
A = list(map(int, input().split()))

from collections import defaultdict
E1 = defaultdict(lambda: defaultdict(lambda: float("inf")))
E2 = defaultdict(lambda: defaultdict(lambda: float("inf")))
for _ in range(M):
    a, b, c = map(int, input().split())
    E1[a][b] = c
    E2[b][a] = c


import heapq
class Dijkstra:
	# 計算量 O((E+V)logV)
 
	# adjは2次元defaultdict
	def dijkstra(self, adj, start, goal=None):
 
		self.dist = defaultdict(lambda: float("inf"))  # 始点から各頂点までの最短距離を格納する
		self.prev = defaultdict(lambda: float("inf"))  # 最短経路における，その頂点の前の頂点のIDを格納する
 
		#num = len(adj)  # グラフのノード数
		#dist = [float('inf') for i in range(num)]
		#prev = [float('inf') for i in range(num)]
 
		self.dist[start] = 0
		q = []  # プライオリティキュー．各要素は，(startからある頂点vまでの仮の距離, 頂点vのID)からなるタプル
		heapq.heappush(q, (0, start))  # 始点をpush
 
		while len(q) != 0:
			prov_cost, src = heapq.heappop(q)  # pop
 
			# プライオリティキューに格納されている最短距離が，現在計算できている最短距離より大きければ，distの更新をする必要はない
			if self.dist[src] < prov_cost:
				continue
 
			# 探索で辺を見つける場合ここに書く
 
			# 他の頂点の探索
			for dest, cost in adj[src].items():
				if self.dist[dest] > self.dist[src] + cost:
					self.dist[dest] = self.dist[src] + cost  # distの更新
					heapq.heappush(q, (self.dist[dest], dest))  # キューに新たな仮の距離の情報をpush
					self.prev[dest] = src  # 前の頂点を記録
 
		if goal is not None:
			return self.get_path(goal, self.prev)
		else:
			return self.dist
 
	def get_path(self, goal, prev):
		path = [goal]  # 最短経路
		dest = goal
 
		# 終点から最短経路を逆順に辿る
		while prev[dest] != float('inf'):
			path.append(prev[dest])
			dest = prev[dest]
 
		# 経路をreverseして出力
		return list(reversed(path))


d1=Dijkstra()
di1=d1.dijkstra(E1, 1)
d2=Dijkstra()
di2=d2.dijkstra(E2, 1)
ans=0
for i, a in enumerate(A, 1): #初期indexが第２引数
	ans = max(ans, (T-di1[i]-di2[i])*a)
print(ans)






