from collections import deque
N=int(input())
G=[[] for _ in range(N)]
for i in range(N-1):
	u, v, w = map(int, input().split())
	u,v=u-1,v-1
	G[u].append([v,w])
	G[v].append([u,w])
#print(G) #[[[1, 2]], [[0, 2], [2, 1]], [[1, 1]]]
color=[-1]*N
que=deque([0])
color[0]=0

while que:#dfs
	p=que.popleft()#直近で追加したグラフの頂点を取得
	for q, W in G[p]:#結合しているグラフの頂点を参照
		if color[q]==-1:#塗られていないなら
			color[q]=(color[p]+W)%2
			que.append(q)
print(*color, sep="\n")