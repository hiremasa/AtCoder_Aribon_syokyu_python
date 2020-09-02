n = int(input())
a = list(map(int, input().split()))

dp = [float("inf")] * n

# dp[i] := 長さが i + 1 であるような増加部分列における最終要素の最小値（存在しない場合は INF）
for j in range(n): #a
	for i in range(n): #dp
		if i==0 or dp[i-1]<a[i]:
			dp[i]=min(dp[i], a[j])

res = 0
for i in dp:
	if i<float("inf"):
		res+=1

print(res)




##########################
#2分探索

#リストseqからLISの長さを出す
seq=list(map(int, input().split()))
import bisect

LIS = [seq[0]]
for i in range(len(seq)):
    if seq[i] > LIS[-1]:
        LIS.append(seq[i])
    else:
        LIS[bisect.bisect_left(LIS, seq[i])] = seq[i]

print(len(LIS))



from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))

dp = [float("inf")] * n

# dp[i] := 長さが i + 1 であるような増加部分列における最終要素の最小値（存在しない場合は INF）
for i in range(n):
    dp[bisect_left(dp, a[i])] = a[i]

print(bisect_left(dp, float("inf")))