from collections import deque
import copy
from functools import lru_cache
H, W = map(int, input().split())
C=list(list(input()) for i in range(H))

road=[]
wall_count=0
for i in range(H):
	for j in range(W):
		if C[i][j]=="s":
			sx, sy = i, j
		if C[i][j]=="g":
			gx, gy = i, j
		if C[i][j]=="#":
			wall_count+=1


all_loc=[[x,y] for x in range(H) for y in range(W)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for p, q in all_loc:
	if C[p][q]!="#":
		continue
	for r, s in all_loc:
		if C[r][s]!="#":
			continue
		D=copy.deepcopy(C)
		D[p][q]="."
		D[r][s]="."

		que=deque()
		que.append([sx, sy])
		visit=[[float("inf")]*W for _ in range(H)]
		visit[sx][sy]=1

		while que:
			x, y = que.popleft()

			for i in range(4):
				nx, ny = x+dx[i], y+dy[i]
				if 0<=nx<H and 0<=ny<W and visit[nx][ny]==float("inf") and D[nx][ny]!="#":

					if nx==gx and ny==gy:
						exit(print("YES"))
					que.append([nx, ny])
					visit[nx][ny]=1
print("YES" if wall_count==0 else "NO")



###############@other's answer###############
H, W = map(int, input().split())
C = [input() for _ in range(H)]
Closed = [[False]*W for _ in range(H)]
for y, s in enumerate(C):
	for x, c in enumerate(s):
		if c=="s":
			start = y, x
			Closed[y][x] = True
		elif c=="g":
			goal = y, x
q = [start]
Dy, Dx = [0,1,0,-1], [1,0,-1,0]
for i in range(3):
	q_new = []
	while q:
		y, x = q.pop()
		if (y, x) == goal:
			print("YES")
			exit()
		for dy, dx in zip(Dy, Dx):
			y_, x_ = y+dy, x+dx
			if 0<=y_<H and 0<=x_<W and not Closed[y_][x_]:
				if C[y_][x_]=="#":
					q_new.append((y_, x_))
				else:
					q.append((y_, x_))
				Closed[y_][x_] = True
	q = q_new
else:
	print("NO")



###############@0 1 BFS###############
from collections import deque
H, W = map(int, input().split())
C=[input() for i in range(H)]
for i in range(H):
	for j in range(W):
		if C[i][j]=="s":
			sx, sy = i, j
		if C[i][j]=="g":
			gx, gy = i, j


# 距離＝壁マスを通る回数 として最短路問題を解く。
dist = [[10**9]*W for i in range(H)]
dist[sx][sy] = 0
# dequeを使って01-BFS
que=deque()
que.append((sx, sy))

while len(que)>0:
	i, j = que.popleft()
	# 4方向の遷移
	for i2, j2 in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
		if not (0 <= i2 < H and 0 <= j2 < W):
			continue
		#この経路での始点から遷移先までの距離。壁なら+1
		wall = (C[i][j]=="#")
		d=dist[i][j]+wall

		#暫定距離より短い経路が得られた場合は更新して、+1なら後ろに、+0なら前に付ける
		if d<dist[i2][j2]:
			dist[i2][j2]=d
			if wall:
				que.append((i2,j2))
			else:
				que.appendleft((i2,j2))
#終点までの距離が2以下ならYES
if dist[gx][gy] <= 2:
	print("YES")
else:
	print("NO")





