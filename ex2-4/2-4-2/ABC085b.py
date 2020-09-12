N=int(input())
D=[int(input()) for _ in range(N)]

se=set([])
for d in D:
	se.add(d)
print(len(se))


#もっと短く書ける
N=int(input())
print(len(set(input() for _ in range(N))))

set(input() for _ in range(N))