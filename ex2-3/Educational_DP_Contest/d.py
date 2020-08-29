N, W = map(int, input().split())
wv=[list(map(int, input().split())) for _ in range(N)]


def solveDP(N, W, value, weight):
    dp = np.zeros((N+1, W+1))
    
    for i in range(N):
        for w in range(W+1):
            if w >= weight[i]:
                dp[i + 1, w] = max(dp[i, w - weight[i]] + value[i], dp[i, w])
            else:
                dp[i + 1, w] = dp[i, w]
    
    return dp[N , W]


"""

import numpy as np
N,W = map(int,input().split())
 
dp=np.zeros(W-1, dtype=np.int64)
for _ in range(N):
	w, v = map(int, input().split())



for _ in range(N):
    w,v = map(int,input().split())
    np.maximum(dp[w:], dp[:-w] + v, out = dp[w:])
 
answer = dp.max()
print(answer)