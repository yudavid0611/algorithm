# 16928: 뱀과 사다리 게임

import sys
sys.stdin = open('16928_input.txt')
from collections import defaultdict

N, M = map(int, input().split())
dp = [0] * 101
dp[1] = 1
ladder = defaultdict(int)
snake = defaultdict(int)

# 사다리
for _ in range(N):
    s, e = map(int, input().split())
    dp[s] = 100
    ladder[s] = e

# 뱀
for _ in range(M):
    s, e = map(int, input().split())
    dp[s] = 100
    snake[s] = e

ladder_start = list(ladder.keys())
snake_start = list(snake.keys())

idx = 2

while idx != 101:    
    # idx에서 1~6칸 전의 값 중 최소값
    turn = min(dp[idx-6:idx]) + 1 if idx > 7 else min(dp[1:idx]) + 1
    
    if dp[idx] and dp[idx] != 100:
        turn = min(turn, dp[idx])
    
    # idx 칸이 사다리 시작점일 경우
    if idx in ladder_start:
        if dp[ladder[idx]]:
            if turn < dp[ladder[idx]]:
                dp[ladder[idx]] = turn
                idx = ladder[idx] + 1
                continue
        else:
            dp[ladder[idx]] = turn
    # idx 칸이 사다리 시작점일 경우
    elif idx in snake_start:
        if dp[snake[idx]]:
            if turn < dp[snake[idx]]:
                dp[snake[idx]] = turn
                idx = snake[idx] + 1
                continue
        else:
            dp[snake[idx]] = turn
    else:
        dp[idx] = turn
    idx += 1
print(dp)