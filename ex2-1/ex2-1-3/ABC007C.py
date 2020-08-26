H, W = map(int, input().split())
sy, sx= map(int, input().split())
gy, gx= map(int, input().split())
sy-=1
sx-=1
gx-=1
gy-=1
C=list(list(input()) for _ in range(H))

from collections import deque

def bfs():
	visited=[[float("inf")]*W for _ in range(H)]
	dx = [1, 0, -1, 0]
	dy = [0, 1, 0, -1]

	work_queue=deque([])

    #初期化
	work_queue.append((sy, sx))
	visited[sy][sx]=0 

	while work_queue:
		y, x=work_queue.popleft()

		for i in range(4):
			ny, nx= y+dy[i], x+dx[i]

			if 0<=ny<H and 0<=nx<W and visited[ny][nx]==float("inf") and C[ny][nx]!="#":
				work_queue.append([ny,nx])
				visited[ny][nx]=visited[y][x]+1 #始点からの距離
	return visited[gy][gx]

print(bfs())
