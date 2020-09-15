from ABC040d import Uf
N, K = map(int, input().split())
uf=Uf(N*3)
"""
「xとyは同じ種」という情報が入ってくるとx-Aとy-Aは互いに連結、x-Bとy-B、x-Cとy-Cも同じく互いに連結
「xはyを食べる」という情報が入ってくるとx-Aとy-Bは互いに連結、x-Bとy-C、x-Cとy-Aも同じく互いに連結
その上で「xはyを食べる」という情報が入ってきた時すでにx-Aとy-Aが連結であったりした場合、情報が矛盾するので無視することになる
"""

ans=0
for i in range(K):
	t, x, y = map(int, input().split())
	x-=1; y-=1

	#正しくない番号
	if x<0 or N<=x or y<0 or N<=y:
		ans+=1
		continue

	elif t==1:
		#xとyは同じ種類という情報
		#矛盾
		if uf.root(x)==uf.root(y+N) or uf.root(x)==uf.root(y+2*N):
			ans+=1

		else:
			uf.unite(x, y)
			uf.unite(x+N, y+N)
			uf.unite(x+2*N, y+2*N)

	else:
		#xはyを食べる
		#矛盾
		if uf.root(x)==uf.root(y) or uf.root(x)==uf.root(y+2*N):
			ans+=1
		else:
			uf.unite(x, y+N)
			uf.unite(x+N, y+2*N)
			uf.unite(x+2*N, y)
print(ans)