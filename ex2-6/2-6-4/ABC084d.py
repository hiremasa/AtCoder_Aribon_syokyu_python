# nまでの自然数が素数かどうかを表すリストを返す
def makePrimeChecker(n):
	isPrime = [True] * (n + 1)
	isPrime[0] = False
	isPrime[1] = False
	for i in range(2, int(n ** 0.5) + 1):
		if isPrime[i]:
			for j in range(i * i, n + 1, i):
				isPrime[j] = False
	return isPrime



isPrime = makePrimeChecker(100000)
Q = int(input())
L=[0]

#2017nunberの累積和
for i in range(100000):
	if i&1==1 and isPrime[i] and isPrime[(i+1)//2]:
		L.append(L[-1]+1)
	else:
		L.append(L[-1])

for i in range(Q):
	l, r = map(int, input().split())
	print(L[r] - L[l-1])