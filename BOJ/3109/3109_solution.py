import sys
sys.stdin = open('3109_input.txt')
input = sys.stdin.readline

R, C = map(int, input().split())
village = [input().rstrip() for _ in range(R)]

visited = [[0] * C for _ in range(R)]
answer = 0

# 우-상/우/우-하
delta = [[-1, 1], [0, 1], [1, 1]]

for i in range(R):
    stack = []
    row = i
    col = 0
    # 이미 방문했거나 건물이 있는 경우
    if visited[row][col] == 1 or village[row][col] == 'x':
        continue
    visited[row][col] = 1

    while True:
        # 빵집에 도달한 경우
        if col == C - 1:
            answer += 1
            break

        for d in delta:
            new_row = row + d[0]
            new_col = col + d[1]

            # 유효한 인덱스 & 건물 없음 & 방문하지 않음
            if 0 <= new_row < R and 0 <= new_col < C and village[new_row][new_col] != 'x' and visited[new_row][new_col] == 0:
                stack.append([row, col])
                row, col = new_row, new_col
                visited[row][col] = 1
                break
        
        # 더 이상 움직일 곳이 없을 경우
        else:
            # 스택에 돌아갈 곳이 없을 경우
            if not stack:
                break
            else:
                row, col = stack.pop()
print(answer)