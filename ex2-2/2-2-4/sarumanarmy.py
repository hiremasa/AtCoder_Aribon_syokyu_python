N=int(input())
R=int(input())
X=sorted(list(map(int, input().split())))

i=0
ans=0
while i<N:
	end=X[i]+R

	while i<N and X[i]<=end:
		i+=1
	#iはstart＋Rを超えた点

	second_end=X[i-1]+R
	while i<=N and X[i]<=second_end:
		i+=1
	ans+=1
print(ans)