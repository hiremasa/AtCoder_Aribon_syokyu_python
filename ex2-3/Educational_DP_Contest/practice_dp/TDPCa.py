N=int(input())
P=list(map(int, input().split()))
W=len(P)

dp=[[False]*(100*101) for _ in range(N+1)]
DP[0][0] = True

for i in range(1, N+1):
	for j, dpj in enumerate(dp[i-1]):
		

"""
se=set([0])
for p in P:
	se |= set(x+p for x in se)
print(len(se))
"""

# 1問目からN問目までのループ
for i in range(1, N+1):
    # DP[i]に値を入れていくために、DP[i-1]の状態を見ていく
    for j, dpj in enumerate(DP[i-1]):
        if dpj is True:
            # i問目の問題を解かない
            DP[i][j] = True

            # i問目の問題を解く
            # i問目の得点はP[i-1]で表される
            DP[i][j+P[i-1]] = True

ans = 0
# DP[N]の配列を見て、Trueになっているところがありうる合計点
for dpi in DP[N]:
    if dpi is True:
        ans += 1
print(ans)