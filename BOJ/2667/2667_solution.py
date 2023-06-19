import sys
from collections import defaultdict

sys.stdin = open('2667_input.txt')

## 접근법 ##
# 1. visited 2차원 리스트를 정의하여 단지를 체크한다.
# 2. 2차원 리스트를 순회하며 아직 체크가 되지 않았고, 집이 존재하는 경우
#   해당 위치부터 단지를 조성한다(DFS).
# 3. 단지 조성이 끝나면 2번 과정이 시작된 다음 위치부터 순회를 이어간다.
# 빠른 출력을 위해 각 단지별 집의 수를 단지가 조성될 떄마다 기록해둔다(딕셔너리).  

N = int(input())

houses = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

# 단지 체크 결과를 기록할 리스트
visited = [[0] * N for _ in range(N)]

# 최종 결과를 정리할 딕셔너리(단지: 집 개수)
result = defaultdict(int)
group = 0

# 방문한 정점을 저장할 스택
stack = [0] * N ** 2
top = -1

# 상, 우, 하, 좌 방향 탐색을 위한 delta 정의
delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]

# 방문 정점 저장 스택
for i in range(N):
    for j in range(N):

        # 이미 체크된 곳이거나 집이 없을 경우 다음 위치로
        if visited[i][j] or not houses[i][j]:
            continue
    
        row, col = i, j

        while True:
            # 되돌아가야 하는지를 표시하는 flag
            go_back = True

            # 아직 방문하지 않은 정점일 경우
            if not visited[row][col]:
                result[group] += 1
                visited[row][col] = 1

            for d in delta:
                next_row, next_col = row + d[0], col + d[1]
                # 상, 우, 하, 좌 방향으로 움직일 수 있는 유효한 정점이 있는 경우
                if 0 <= next_row < N and 0 <= next_col < N and houses[next_row][next_col] and not visited[next_row][next_col]:
                    # 스택에 현재 정점 추가
                    top += 1
                    stack[top] = [row, col]

                    row, col = next_row, next_col
                    go_back = False
                    break
            
            # 현재 정점에서 이동할 수 있는 정점이 없을 경우
            if go_back:
                # 더 이상 되돌아갈 수 있는 정점이 없을 경우
                if top == -1:
                    if result[group]:
                        group += 1
                    break
                else:
                    row, col = stack[top]
                    stack[top] = 0
                    top -= 1

# 마지막 key의 값이 의미 없는 경우(0일 경우) 제거
if not result[group]:
    del result[group]

# 오름차순 정리
result_asc = sorted(result.values())

# 출력
print(len(result_asc))
for r in result_asc:
    print(r)