n = int(input())
m = int(input())
a = list(map(int, input().split()))
M = int(input())

#dp = [[0] * (m + 1) for i in range(n + 1)]
import numpy as np
##############O(nm)##############
# dp[i + 1][j] := i 番目までの品物から j 個選ぶ組み合わせの総数
dp = np.zeros((n+1,m+1),dtype = int)

# 1 つも選ばない方法は常に一通り
dp[0,:a[0]] = 1
dp[:,0] = 1

for i in range(n):
    for j in range(1,m+1):
    	#引き算が含まれる場合には負の数にならないように注意する
        if j -1 - a[i] >=0:
            dp[i+1][j] = dp[i+1][j-1] + dp[i][j] -dp[i][j-1-a[i]]
        else:
            dp[i+1][j] = dp[i+1][j-1] + dp[i][j]

print(dp[-1][-1])