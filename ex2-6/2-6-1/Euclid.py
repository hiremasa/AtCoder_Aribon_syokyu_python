def gcd(a, b):
	while b:
		a, b = b, a%b
	return a
P=[]
for _ in range(2):
	x, y = map(int, input().split())
	P.append((x, y))

print(gcd(abs(P[0][0]-P[1][0]), abs(P[0][1]-P[1][1])) -1)