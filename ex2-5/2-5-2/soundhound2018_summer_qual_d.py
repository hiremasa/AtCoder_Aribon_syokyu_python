from collections import defaultdict
import heapq
N, M, s, t = map(int, input().split())
Ga = defaultdict(list)
Gb = defaultdict(list)

for _ in range(M):
    u, v, a, b = map(int, input().split())
    Ga[u - 1].append((v - 1, a))
    Gb[u - 1].append((v - 1, b))
    Ga[v - 1].append((u - 1, a))
    Gb[v - 1].append((u - 1, b))

anses = [0] * N
for i in range(N):
    ans = float("inf")
    #aに関して
    #init
    pq = []
    Cost_a = [float("inf")] * N
    Cost_a[s - 1] = 0
    heapq.heappush(pq, (0, s - 1))

    #更新
    while pq:
        cost_a, cur_node = heapq.heappop(pq)
        if cost_a > Cost_a[cur_node]:
            continue
        for next_node, next_a in Ga[cur_node]:
            if Cost_a[cur_node] + next_a < Cost_a[next_node]:
                Cost_a[next_node] = cost_a + next_a
                heapq.heappush(pq, (Cost_a[next_node], next_node))
    ans_a = Cost_a[i]

    #bに関して
    pq = []
    Cost_b = [float("inf")] * N
    Cost_b[t - 1] = 0
    heapq.heappush(pq, (0, t - 1))

    #更新
    while pq:
        cost_b, cur_node = heapq.heappop(pq)
        if cost_b > Cost_b[cur_node]:
            continue
        for next_node, next_b in Gb[cur_node]:
            if Cost_b[cur_node] + next_b < Cost_b[next_node]:
                Cost_b[next_node] = cost_b + next_b
                heapq.heappush(pq, (Cost_b[next_node], next_node))
    ans_b = Cost_b[i]

    ans = min(ans, ans_a + ans_b)

    anses[N - 1- i] = 10**15 - ans

for i in range(N):
    print(anses[i])
