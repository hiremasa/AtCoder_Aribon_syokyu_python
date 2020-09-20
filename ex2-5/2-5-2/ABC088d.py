from collections import deque
H, W = map(int, input().split())
C=list(list(input()) for _ in range(H))

def bfs():
	sx, sy = 0, 0
	gx, gy = H-1, W-1
	dx = [1, 0, -1, 0]
	dy = [0, 1, 0, -1]

	que=deque()
	que.append([sx, sy])
	visit=[[float("inf")]*W for _ in range(H)]
	visit[sx][sy]=1

	while que:
		x, y = que.popleft()
		for i in range(4):
			nx, ny = x+dx[i], y+dy[i]
			if 0<=nx and nx<H and 0<=ny and ny<W and visit[nx][ny]==float("inf") and C[nx][ny]!="#":
				que.append([nx,ny])
				visit[nx][ny]= visit[x][y]+1
	return visit[gx][gy]

black=0
white=0
for i in range(H):
	for j in range(W):
		if C[i][j]=="#":
			black+=1
		else:
			white+=1

temp=bfs()
if temp==float("inf"):
	print(-1)
else:
	ans=white-temp
	print(ans)