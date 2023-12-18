import sys
from heapq import heappush, heappop
sys.stdin = open('10217_input.txt')
input = sys.stdin.readline


T = int(input().rstrip())
N, M, K = map(int, input().split())
routes =[[] for _ in range(N + 1)]
for _ in range(K):
    u, v, cost, time = map(int, input().split())
    routes[u].append([v, cost, time])

# dp에 각 공항의 비용별 최소 도착 시간 저장
init_time = 1000 * N + 1
dp = [[init_time] * (M + 1) for _ in range(N + 1)]
dp[1][0] = 0

heap = []
heappush(heap, [0, 1])
visited = [0] * (N + 1)

while heap:
    # 최소 도착 시간을 가진 공항을 먼저 꺼내기
    _, v = heappop(heap)

    # 이미 방문했던 곳
    if visited[v] == 1:
        continue
    # 방문 표시
    else:
        visited[v] = 1
    
    # 목적지 도착
    if v == N:
        break

    for next_airport, cost, time in routes[v]:
        min_time = init_time
        for i in range(M - cost + 1):
            # 기존 공항에서 비용이 i일 때 최소 시간이 init_time과 동일하면
            # dp 갱신이 절대 발생하지 않음 -> continue
            if dp[v][i] == init_time:
                continue

            min_time = min(min_time, dp[v][i] + time)

            # min_time이 dp에 저장된 값보다 작으면 dp 업데이트
            if dp[next_airport][i + cost] > min_time:
                dp[next_airport][i + cost] = min_time

        # 아직 방문하지 않았고, min_time이 업데이트 된 경우 heap에 push
        if visited[next_airport] == 0 and min_time < init_time:
            heappush(heap, [min_time, next_airport])

if visited[N] == 0:
    print('Poor KCM')
else:
    print(min(dp[N]))