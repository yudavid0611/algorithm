import sys
import heapq
from collections import defaultdict
sys.stdin = open('1939_input.txt')
input = sys.stdin.readline


def djk(s, e):
    q = [[-1000000001, s]]
    visited = [0] * (N + 1)

    while q:
        w, v = heapq.heappop(q)
        w = -w

        # 목적지 도달
        if v == e:
            return w
        # 이미 방문한 정점
        elif visited[v] == 1:
            continue
        else:
            # 방문 표시
            visited[v] = 1

            # 경로 추가
            for v2, w2 in graph[v]:
                # 작은 값으로 넣어줌
                if w >= w2:
                    heapq.heappush(q, [-w2, v2])
                else:
                    heapq.heappush(q, [-w, v2])


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(M):
        v1, v2, w = map(int, input().split())
        graph[v1].append([v2, w])
        graph[v2].append([v1, w])
    
    s, e = map(int, input().split())
    print(djk(s, e))