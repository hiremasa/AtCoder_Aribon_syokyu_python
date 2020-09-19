#https://atcoder.jp/contests/code-festival-2017-qualb/tasks/code_festival_2017_qualb_c
from collections import deque
N,M=map(int,input().split())
G=[[] for i in range(N)]
for i in range(M):
	a,b = map(int,input().split())
	G[a-1].append(b-1)
	G[b-1].append(a-1)
visit=[False]*N
color=[-1]*N
que=deque()

def nibu():
	que.append(0)
	color[0]=1

	while que:
		p=que.pop()
		visit[p]=True
		for q in G[p]:
			if visit[q] and color[q]==color[p]:
				return False
			elif not visit[q]:
				que.append(q)
				color[q]=(color[p]+1)%2
	return True

if nibu():
	B=color.count(0)
	W=color.count(1)
	ans=B*W-M
else:
	ans = (N*(N-1))//2 -M
print(ans)