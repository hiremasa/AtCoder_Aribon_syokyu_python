T=int(input())
S=[input() for _ in range(T)]

word=set(["tokyo", "kyoto"])

for seq in S:
	cnt=0
	i=0
	while i<=len(seq):
		if seq[i:i+5] in word:
			cnt+=1
			i+=5
		else:
			i+=1
	print(cnt)
