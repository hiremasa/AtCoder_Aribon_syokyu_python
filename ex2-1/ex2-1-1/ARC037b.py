import sys
sys.setrecursionlimit(10000000)

N, M = map(int, input().split())
 
G = [[] for _ in range(N)]
 
for _ in range(M):
    u, v = map(int, input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)

visited = [False] * N

def dfs(i, pre):
    visited[i] = True
 
    for j in graph[i]:
        if not visited[j]:
            if not dfs(j, i):
                return False
        elif visited[j] and j == pre:
            continue
        else:
            return False
 
    return True
 


ans = 0
for i in range(N):
    if not visited[i]:
        flag = dfs(i, i)
        if flag:
            ans += 1

print(ans)
