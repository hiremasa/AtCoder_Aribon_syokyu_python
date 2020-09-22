H, W = map(int, input().split())
C=list(list(map(int, input().split())) for _ in range(10))

#d[i][j]は2頂点間i, j間の移動コストを格納, Vは頂点数
def warshall_floyd(d, V): 
	for k in range(V):
		for i in range(V):
			for j in range(V):
				d[i][j] = min(d[i][j], d[i][k] + d[k][j])

	return d #d[i][j]に頂点i, j間の最短距離を格納

d=warshall_floyd(C, 10)

ans=0
for _ in range(H):
	A=list(map(int, input().split()))
	for a in A:
		if a==-1:
			continue
		else:
			ans+=d[a][1]

print(ans)