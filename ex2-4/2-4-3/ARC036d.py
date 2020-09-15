# unionfind
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




N, Q = map(int, input().split())
uf = Uf(2*N) #i番の頂点からi*2番を偶数用、i*2+1番を奇数用とする

for i in range(Q):
    w, x, y, z = map(int, input().split())
    if w == 1:
        #zが偶数なら、2*xと2*y、2*x+1と2*y+1の点をuniteする
        if not z&1:
            # 青
            uf.unite(2*(x-1), 2*(y-1))
            # 赤
            uf.unite(2*(x-1)+1, 2*(y-1)+1)
        #zが奇数なら、2*xと2*y+1、2*xと2*y+1の点をuniteする
        else:
            uf.unite(2*(x-1), 2*(y-1)+1)
            uf.unite(2*(x-1)+1, 2*(y-1))
    else:
        #2*xと2*yがuniteされているかどうか判定する
        if uf.root(2*(x-1)+1) == uf.root(2*(y-1)+1):
            print('YES')
        else:
            print('NO')