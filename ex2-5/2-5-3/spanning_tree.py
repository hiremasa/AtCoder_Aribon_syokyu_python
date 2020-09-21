import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix, coo_matrix, lil_matrix
l = [[0, 8, 0, 3],
	[0, 0, 2, 5],
	[0, 0, 0, 6],
	[0, 0, 0, 0]]
mst = minimum_spanning_tree(l)
print(mst)
#   (0, 3)  3.0
#   (1, 2)  2.0
#   (1, 3)  5.0

print(type(mst))
# <class 'scipy.sparse.csr.csr_matrix'>

#csr_matrixのtoarray()でnumpy.ndarrayに変換できる。
#隣接行列
print(mst.toarray())
# [[0. 0. 0. 3.]
#  [0. 0. 2. 5.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]
print(mst.toarray().astype(int))
# [[0 0 0 3]
#  [0 0 2 5]
#  [0 0 0 0]
#  [0 0 0 0]]
#リストに変換したい場合はさらにnumpy.ndarrayのtolist()を使う。
print(mst.toarray().astype(int).tolist())
# [[0, 0, 0, 3], [0, 0, 2, 5], [0, 0, 0, 0], [0, 0, 0, 0]]

print(type(mst.toarray().astype(int).tolist()))
# <class 'list'>

#重み（コスト）の総和
print(mst.sum())
# 10.0


#クラスカル法
def main():
	V, E = map(int, input().split())
	uf = UnionFind(V)

	# 1の過程
	edges = []
	for _ in range(E):
		s, t, w = map(int, input().split())
		edges.append((w, s, t))
	edges.sort()

	# 2の過程
	cost = 0
	for edge in edges:
		w, s, t = edge
		if not uf.same(s, t):
			cost += w
			uf.union(s, t)
	print(cost)
	return


