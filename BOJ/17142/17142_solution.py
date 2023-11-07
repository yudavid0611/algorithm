import sys
from itertools import combinations
from collections import deque
sys.stdin = open('17142_input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

# 비활성 바이러스 위치 저장
viruses = []
walls = 0
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            viruses.append([i, j])
        elif lab[i][j] == 1:
            walls += 1

# 바이러스를 퍼뜨려야 하는 공간
spaces = N ** 2 - walls - len(viruses)

# 이미 바이러스가 다 퍼진 경우
if spaces == 0:
    print(0)

else:
    min_time = N * N

    # 초기 바이러스 활성화 공간 조합
    candidates = list(combinations(viruses, M))

    # 상, 우, 하, 좌
    delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    for candidate in candidates:
        # 바이러스를 저장할 queue
        spread = deque()

        # 현재 남은 빈 공간
        now_spaces = spaces

        # 방문 처리(바이러스 퍼진 곳 체크)
        visited = [lab[i][:] for i in range(N)]

        # 초기 바이러스 활성화
        for row, col in candidate:
            spread.append([row, col, 0])
            visited[row][col] = 3

        while now_spaces > 0 and spread:
            v_row, v_col, t = spread.popleft()
            
            # min_time 이상인 경우 더 확인할 필요 업음
            if t >= min_time:
                break

            # 빈 공간일 경우 now_space 차감
            if lab[v_row][v_col] == 0:
                now_spaces -= 1

            for d in delta:
                new_r = v_row + d[0]
                new_c = v_col + d[1]
                
                # 유효한 공간일 경우
                if 0 <= new_r < N and 0 <= new_c < N:
                    # 벽 또는 이미 방문한 공간일 경우
                    if visited[new_r][new_c] == 1 or visited[new_r][new_c] == 3:
                        continue
                    else:
                        spread.append([new_r, new_c, t + 1])
                        visited[new_r][new_c] = 3

        # 바이러스가 모두 퍼진 경우
        if now_spaces == 0:
            min_time = t

    if min_time == N * N:
        print(-1)
    else:
        print(min_time)