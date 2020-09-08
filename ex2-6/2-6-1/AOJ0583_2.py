#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0583

N=int(input())
A=list(map(int, input().split()))

def gcd(a, b):
	while b:
		a, b = b, a%b
	return a

g=0
for a in A:
	g=gcd(g, a)

for i in range(1, g+1):
	if g%i==0:
		print(i)
