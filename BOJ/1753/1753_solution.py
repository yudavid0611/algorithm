import sys
import heapq
from collections import defaultdict

sys.stdin = open('1735_input.txt')

## 접근법 ##
# 1. 인접 리스트 만들기(defaultdict)
# 2. heapq 모듈을 사용하여 각 정점별 최소 거리 구하기

V, E = map(int, sys.stdin.readline().split())

START = int(input())

# 인접 리스트
adj = defaultdict(list)

# 최소 거리 저장
min_dist = defaultdict(int)

# 인접 리스트 원소 추가
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    adj[u].append([v, w])

q = []
heapq.heappush(q, [0, START])

while q:
    dist, u = heapq.heappop(q)

    # 방문하지 않은 정점일 경우
    if not min_dist[u]:
        min_dist[u] = dist
    
        for v, w in adj[u]:
            heapq.heappush(q, [w + dist, v])

for i in range(1, V + 1):
    if i == START:
        print(0)
    elif not min_dist[i]:
        print('INF')
    else:
        print(min_dist[i])