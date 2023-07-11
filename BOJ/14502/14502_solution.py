import sys
from itertools import combinations
from collections import deque
sys.stdin = open('14502_input.txt')

def bfs(max_safe_zone:int, safe_zone:int, viruses:list, walls:tuple, lab:list, row_len:int, col_len:int):
    # queue
    q = deque(viruses)
    # 상우하좌
    delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    # 지도
    visited = [i[:] for i in lab]
    # 현재 안전 영역
    now_safe_zone = safe_zone

    # 3개의 벽 지도에 표시
    for w in walls:
        visited[w[0]][w[1]] = 1

    while q and now_safe_zone > max_safe_zone:
        row, col = q.popleft()
        
        # 바이러스가 퍼졌으니 안전 영역 -1
        now_safe_zone -= 1

        for d in delta:
            new_row = row + d[0]
            new_col = col + d[1]

            if 0 <= new_row < row_len and 0 <= new_col < col_len and visited[new_row][new_col] == 0:
                q.append([new_row, new_col])
                visited[new_row][new_col] = 2
                
    if now_safe_zone > max_safe_zone:
        return now_safe_zone
    else:
        return max_safe_zone


N, M = map(int, sys.stdin.readline().split())

lab = []
zero_position = []
safe_zone = 0
viruses = []
for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    lab.append(row)

    for idx, r in enumerate(row):
        # 안전 구역일 경우
        if r == 0:
            zero_position.append([i, idx])
            safe_zone += 1
        # 바이러스가 위치한 곳일 경우
        elif r == 2:
            viruses.append([i, idx])

max_safe_zone = 0

# bfs에서 초기 바이러스에 대해서도 안전 영역 -1을 해주기 때문에 바이러스 수만큼 더해줌
# 그리고 새로 세울 벽의 개수인 3은 미리 빼줌
safe_zone += len(viruses) - 3

# 벽을 세울 수 있는 조합 구하기
wall_cbn = list(combinations(zero_position, 3))

for wall in wall_cbn:
    max_safe_zone = bfs(max_safe_zone, safe_zone, viruses, wall, lab, N, M)

print(max_safe_zone)