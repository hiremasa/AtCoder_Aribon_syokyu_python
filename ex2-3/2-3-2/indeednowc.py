n, m = map(int, input().split())

# 能力値は 0 ~ 100 の 101 通り
#dp[i][j][k] := 技術力 a, 語学力 j, コミュ力 k のときの最高年収
dp = [[[-1] * 102 for i in range(102)] for j in range(102)]
#dpを更新する
for i in range(n):
	a, b, c, w =map(int, input().split())
	dp[a][b][c] = max(dp[a][b][c], w)

for a in range(101):  # 能力値は 0 ~ 100
    for j in range(101):
        for k in range(101):
            # 能力が高ければそれより要求能力の低い求人は応募できる
            dp[a + 1][j][k] = max(dp[a + 1][j][k], dp[a][j][k])
            dp[a][j + 1][k] = max(dp[a][j + 1][k], dp[a][j][k])
            dp[a][j][k + 1] = max(dp[a][j][k + 1], dp[a][j][k])

for i in range(m):
    x, y, z = map(int, input().split())
    print(dp[x][y][z])