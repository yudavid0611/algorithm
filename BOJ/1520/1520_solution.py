import sys
from collections import deque
sys.stdin = open('1520_input.txt')

N, M = map(int, sys.stdin.readline().split())

map_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
memo = [[-1] * M for _ in range(N)]

delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def dfs(r, c):
    # 도착지 정점일 경우
    if r == N - 1 and c == M - 1:
        return 1
    
    # 이전에 방문한 정점인 경우
    elif memo[r][c] != -1:
        return memo[r][c]
    
    # 정점 방문 표시
    memo[r][c] = 0
    for d in delta:
        new_r = r + d[0]
        new_c = c + d[1]

        # 유효한 정점일 경우
        if 0 <= new_r < N and 0 <= new_c < M and map_list[r][c] > map_list[new_r][new_c]:
            memo[r][c] += dfs(new_r, new_c)
    return memo[r][c]
       
print(dfs(0, 0))