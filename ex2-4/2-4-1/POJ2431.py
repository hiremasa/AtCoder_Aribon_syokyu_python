import heapq
N, L, P = map(int, input().split()) #N:ガソリンスタンドの個数 ,L:距離, P:距離
A=list(map(int, input().split()))
B=list(map(int, input().split()))

#-1倍したB[i]を入れる優先度付きキュー
C=[]
#ans:補給回数, pos:今いる場所, tank:タンクのガソリンの量
ans=0
pos=0
tank=P

for i in range(N):
	d=A[i]-pos #次に進む距離

	#十分な量になるまでガソリンを補給
	while tank<d:
		if len(C)==0:
			exit(print(-1))
		tank += -heapq.heappop(C)
		ans+=1

	tank-=d
	pos=A[i]
	heapq.heappush(C, -B[i])
print(ans)
