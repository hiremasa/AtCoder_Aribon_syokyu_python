A=list(list(input()) for _ in range(10))

land=[]
num_land=0
for i in range(10):
	for j in range(10):
		if A[i][j]=="o":
			land.append((i, j))
			num_land+=1


all_loc=[[x, y] for x in range(10) for y in range(10)]
dx_dy=[[1,0], [-1,0], [0,1], [0,-1]]

#DFS
for loc in all_loc:
	if loc in land:
		continue
	work_stack=[loc]#初期化
	visited=[[0]*10 for _ in range(10)]
	visited[loc[0]][loc[1]]=1
	cnt=0

	while work_stack:
		x, y = work_stack.pop()
		for i in range(4):
			#現在地
			nx, ny= x+dx_dy[i][0], y+dx_dy[i][1]

			#更新: はみ出していない＆訪れていない＆移動できる
			if 0<=nx<10 and 0<=ny<10 and visited[nx][ny]==0 and A[nx][ny]!="x":
				work_stack.append([nx,ny])
				visited[nx][ny]=1
				cnt+=1

		if cnt==num_land:
			print("YES")
			exit()
print("NO")