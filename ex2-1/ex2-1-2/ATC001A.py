H, W = map(int, input().split())
C=list(list(input()) for _ in range(H))

#s, g探し
for i in range(H):
	for j in range(W):
		if C[i][j]=="s":
			sx, sy = i, j
		elif C[i][j]=="g":
			gx, gy = i, j

work_stack=[]
work_stack.append([sx, sy])
visited=[[0]*W for _ in range(H)]
visited[sx][sy]=1
dx_dy=[[1,0], [-1,0], [0,1], [0,-1]]

#DFS
while work_stack:
	x, y = work_stack.pop()
	for i in range(4):
		#現在地
		nx, ny= x+dx_dy[i][0], y+dx_dy[i][1]

		#更新: はみ出しでいない＆訪れていない＆移動できる
		if 0<=nx<H and 0<=ny<W and visited[nx][ny]==0 and C[nx][ny]!="#":
			work_stack.append([nx,ny])
			visited[nx][ny]=1

	if visited[gx][gy]==1:
		print("Yes")
		exit()
print("No")
