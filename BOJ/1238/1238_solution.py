import sys
from collections import defaultdict
import heapq


sys.stdin = open('1238_input.txt')
input = sys.stdin.readline


# 다익스트라 함수
def djk(adj_list, min_time):
    q = []
    heapq.heappush(q, [0, X])
    visited = [0] * (N + 1)
    flag = 0

    while q:
        agg_time, v = heapq.heappop(q)

        # 이미 방문한 마을일 경우
        if visited[v] == 1:
            continue

        # 아직 방문하지 않은 마을일 경우
        else:
            # 누적 시간 더해주기
            min_time[v] += agg_time
            # 방문 표시
            visited[v] = 1
            # 방문한 마을 개수 + 1
            flag += 1
            if flag == N:
                break
            
            # 경로 추가
            for next_v, next_time in adj_list[v]:
                heapq.heappush(q, [agg_time + next_time, next_v])

    return min_time


if __name__ == '__main__':
    N, M, X = map(int, input().split())
    adj_list_forward = defaultdict(list)
    adj_list_reversed = defaultdict(list)
    for _ in range(M):
        start, end, t = map(int, input().split())
        adj_list_forward[start].append([end, t])
        adj_list_reversed[end].append([start, t])

    min_time = [0] * (N + 1)

    # X까지 가는 최소 시간: 뒤집힌 간선으로 X에서 출발
    min_time = djk(adj_list_reversed, min_time)

    # X로부터 돌아오는 최소 시간: 기존 간선으로 X에서 출발
    min_time = djk(adj_list_forward, min_time)

    print(max(min_time[1:]))