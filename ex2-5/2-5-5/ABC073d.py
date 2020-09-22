import itertools
N, M, R = map(int, input().split())
r=[int(x) for x in input().split()]
r=[i-1 for i in r]
d=[[float("inf")]*N for _ in range(N)]
for i in range(N):
	d[i][i]=0
for _ in range(M):
	a, b, c = map(int, input().split())
	a-=1
	b-=1
	d[a][b]=min(d[a][b], c)
	d[b][a]=min(d[b][a], c)

#d[i][j]は2頂点間i, j間の移動コストを格納, Vは頂点数
def warshall_floyd(d, V): 
	for k in range(V):
		for i in range(V):
			for j in range(V):
				d[i][j] = min(d[i][j], d[i][k] + d[k][j])

	return d #d[i][j]に頂点i, j間の最短距離を格納

d=warshall_floyd(d, N)
ans=float("inf")
for l in list(itertools.permutations(r)):
	temp=sum([d[l[i]][l[i+1]] for i in range(R-1)])
	ans=min(ans, temp)
print(ans)