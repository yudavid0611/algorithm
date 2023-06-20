import sys
sys.stdin = open('2178_input.txt')

from collections import deque

## 접근법 ##
# 탐색 종료 조건: 도착지점 도착 / 거리가 최소 칸수를 넘음
# bfs 방식으로 접근
# 1. 큐를 정의한다.
# 2. (1,1)을 시작으로 이동가능한 거리를 큐에 추가해간다.
#   이때, 이동 거리도 함께 저장한다.
# 3. 이동 가능한 정점을 추가할 때, 추가될 정점까지 도달하는 기존 최소 거리와 비교하여
#   더 짧을 때만 해당 정점을 추가한다.

N, M = map(int, input().split())

# 상, 우, 하, 좌
delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]

# 미로 input 받기
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

# 각 정점까지의 최소 거리를 저장할 리스트
dist_map = [[N * M] * M for _ in range(N)]

# 큐 정의. 첫 번째 원소 리스트는 좌표, 두 번째 원소는 거리
q = deque()
q.append([[0, 0], 1])

while q:
    position, dist = q.popleft()
    row, col = position

    # 도착지점에 도착한 경우
    if row == N-1 and col == M-1:
        dist_map[row][col] = dist
        continue

    for d in delta:
        next_row, next_col = row + d[0], col + d[1]
        
        # 유효한 좌표이고, 이동할 수 있는 정점이고, 정점까지 거리가 짧아질 경우
        # 큐에 정점 추가
        if 0 <= next_row < N and 0 <= next_col < M and maze[next_row][next_col] and (dist + 1) < dist_map[next_row][next_col]:
            dist_map[next_row][next_col] = dist + 1
            q.append([[next_row, next_col], dist + 1])

print(dist_map[N-1][M-1])