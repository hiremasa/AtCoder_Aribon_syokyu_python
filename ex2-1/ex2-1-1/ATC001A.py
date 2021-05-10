import sys
sys.setrecursionlimit(1000000)

H, W = map(int, input().split())
G = [list(input()) for i in range(H)]
visited = [[0] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if G[i][j] == "s":
            sx, sy = i, j # スタート位置


def DFS(i, j):
    if not(0 <= i < H) or not(0 <= j < W) or (G[i][j] == "#") or visited[i][j] == 1:
        return


    if G[i][j] == "g":
        exit(print("Yes"))
    G[i][j] = "#"
    DFS(i + 1, j)
    DFS(i, j + 1)
    DFS(i - 1, j)
    DFS(i, j - 1)

DFS(sx, sy)
print("No")
