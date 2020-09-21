A=list(list(input()) for _ in range(10))
from collections import defaultdict, deque
land=[]
num_land=0

for i in range(10):
	for j in range(10):
		if A[i][j]=="o":
			land.append([i, j])
			num_land+=1

all_loc=[[x,y] for x in range(10) for y in range(10)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for sx, sy in all_loc:
	if [sx, sy] in land:
		continue
	cnt=0
	que=deque()
	que.append([sx, sy])
	visit=[[float("inf")]*10 for _ in range(10)]
	visit[sx][sy]=1

	while que:
		x, y = que.popleft()
		for i in range(4):
			nx, ny = x+dx[i], y+dy[i]
			if 0<=nx and nx<10 and 0<=ny and ny<10 and visit[nx][ny]==float("inf") and A[nx][ny]=="o":
				visit[nx][ny]=1
				que.append([nx, ny])
				cnt+=1

		if cnt==num_land:
			exit(print("YES"))

print("NO")


