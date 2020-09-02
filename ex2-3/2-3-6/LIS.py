n = int(input())
a = list(map(int, input().split()))

dp = [float("inf")] * n

# dp[i] := 長さが i + 1 であるような増加部分列における最終要素の最小値（存在しない場合は INF）
for j in range(n):
	for i in range(n):
		if i==0 or dp[i-1]<a[i]:
			dp[i]=min(dp[i], a[j])

res = 0
for i in dp:
	if i<float("inf"):
		res+=1

print(res)