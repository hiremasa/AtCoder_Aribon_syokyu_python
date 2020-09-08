N=int(input())
T=list(int(input()) for _ in range(N))

def gcd(a, b):
	while b:
		a, b = b, a%b
	return a

l=T[0]
for t in T:
	l=l // gcd(l, t) * t
print(l)