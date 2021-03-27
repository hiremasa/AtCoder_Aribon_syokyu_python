N, D = map(int, input().split())

A = B = C = 0
while D % 2 == 0:
    D //= 2
    A += 1
while D % 3 == 0:
    D //= 3
    B += 1
while D % 5 == 0:
    D //= 5
    C += 1
 
if D > 1:
    print(0)
    exit()

dp = [[[[0] * (C + 1) for _ in range(B + 1)] for _ in range(A + 1)] for _ in range(N + 1)]
dp[0][0][0][0] = 1

for i in range(N):
    for a in range(A + 1):
        for b in range(B + 1):
            for c in range(C + 1):
                temp = dp[i][a][b][c] / 6
                dp[i + 1][min(a + 0, A)][min(b + 0, B)][min(c + 0, C)] += temp
                dp[i + 1][min(a + 1, A)][min(b + 0, B)][min(c + 0, C)] += temp
                dp[i + 1][min(a + 0, A)][min(b + 1, B)][min(c + 0, C)] += temp
                dp[i + 1][min(a + 2, A)][min(b + 0, B)][min(c + 0, C)] += temp
                dp[i + 1][min(a + 0, A)][min(b + 0, B)][min(c + 1, C)] += temp
                dp[i + 1][min(a + 1, A)][min(b + 1, B)][min(c + 0, C)] += temp
print(dp[N][A][B][C])

