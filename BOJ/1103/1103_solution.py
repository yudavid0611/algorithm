'''
visited를 깊은 복사 하는 과정에서 deepcopy 함수를 사용했다.
제출 시 시간초과가 발생했는데, deepcopy의 시간복잡도를 찾아보니
슬라이싱으로 복사하는 것보다 크게는 100여배나 느리다는 사실을 발견했다.
이를 고려하여 슬라이싱 방식으로 변경하여 문제를 통과할 수 있었다.
'''

import sys
from collections import deque
sys.stdin = open('1103_input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

def change_type(char):
    try:
        return int(char)
    except:
        return 0

board = []
for _ in range(N):
    i_str = list(input().rstrip())
    board.append(list(map(change_type, i_str)))

queue = deque()
dp = [[0] * M for _ in range(N)]

visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
queue.append([[0, 0], 0, visited])

# 상, 우, 하, 좌
delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]

infinite = False
while queue and not infinite:
    coin, moved, visited = queue.popleft()

    for d in delta:
        new_row = coin[0] + d[0] * board[coin[0]][coin[1]]
        new_col = coin[1] + d[1] * board[coin[0]][coin[1]]
        
        # 유효한 칸인지 확인
        if 0 <= new_row < N and 0 <= new_col < M:
            
            # 구멍이 아닌지 확인
            if board[new_row][new_col] != 0:

                # 이미 방문한 곳인 경우
                if visited[new_row][new_col] == 1:
                    infinite = True
                    print(-1)
                    break
                
                # 아직 방문하지 않은 곳일 경우
                else:
                    # dp 업데이트
                    new_moved = moved + 1
                    if dp[new_row][new_col] < new_moved:
                        dp[new_row][new_col] = new_moved
                    
                        # queue에 추가
                        visited_new = [i[:] for i in visited]
                        visited_new[new_row][new_col] = 1
                        queue.append([[new_row, new_col], new_moved, visited_new])

if not infinite:
    max_moved = 0
    for i in range(N):
        for j in range(M):
            if dp[i][j] > max_moved:
                max_moved = dp[i][j]
    print(max_moved + 1)