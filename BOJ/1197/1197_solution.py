import sys
import heapq
from collections import defaultdict
sys.stdin = open('1197_input.txt')
input = sys.stdin.readline

V, E = map(int, input().split())
adj_list = defaultdict(list)
for _ in range(E):
    a, b, c = map(int, input().split())
    # 무방향 그래프이기 때문에 양방향으로 이동 가능
    adj_list[a].append([b, c])
    adj_list[b].append([a, c])

# 정점이 하나일 경우
if V == 1:
    print(adj_list[1][0][1])

# 정점이 2개 이상일 경우
else:
    # 방문한 정점 처리
    mst = [0] * (V + 1)
    
    # 시작 정점
    v = 1

    # 방문한 정점 개수
    mst_count = 1
    mst[v] = 1

    # 우선순위 큐로 활용할 리스트
    q = []

    # 출력값 초기화
    sum_weight = 0

    while mst_count < V:
        # 인접 정점 추가
        for v_adj in adj_list[v]:
            # 아직 방문하지 않은 정점일 경우 q에 추가
            if mst[v_adj[0]] == 0:
                heapq.heappush(q, [v_adj[1], v_adj[0]])

        while q:
            weight, v_next = heapq.heappop(q)

            # 아직 방문하지 않은 정점일 경우
            if mst[v_next] == 0:
                mst[v_next] = 1
                mst_count += 1
                sum_weight += weight
                v = v_next
                break

    print(sum_weight)