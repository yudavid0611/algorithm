# 16928: 뱀과 사다리 게임

import sys
sys.stdin = open('16928_input.txt')
from collections import defaultdict

N, M = map(int, input().split())
dp = [0] * 101

ladder = defaultdict(int)
snake = defaultdict(int)

# 사다리: 시작점-key, 도착점-value
for _ in range(N):
    s, e = map(int, input().split())
    dp[s] = 100
    ladder[s] = e

# 뱀: 시작점-key, 도착점-value
for _ in range(M):
    s, e = map(int, input().split())
    dp[s] = 100
    snake[s] = e

# 키들만 따로 저장
ladder_start = list(ladder.keys())
snake_start = list(snake.keys())

idx = 1
while idx != 101:    
    # idx 칸에서 1~6칸 전의 값 중 최소값
    turn = min(dp[idx-6:idx]) + 1 if idx > 7 else min(dp[:idx]) + 1
    
    # 이미 idx 칸에 값이 존재할 경우
    if dp[idx] and dp[idx] != 100:
        turn = min(turn, dp[idx])
    
    # idx 칸이 사다리 시작점일 경우
    if idx in ladder_start:
        # 이미 사다리 도착점에 값이 있을 경우
        if dp[ladder[idx]]:
            # 신규 값이 더 작을 경우 업데이트
            if turn < dp[ladder[idx]]:
                dp[ladder[idx]] = turn
                continue
        # 사다리 도착점에 값이 없을 경우
        else:
            dp[ladder[idx]] = turn

    # idx 칸이 뱀 시작점일 경우
    elif idx in snake_start:
        # 이미 뱀 도착점에 값이 있을 경우
        if dp[snake[idx]]:
            # 신규 값이 더 작을 경우 업데이트
            if turn < dp[snake[idx]]:
                dp[snake[idx]] = turn
                # 값이 업데이트되었기 때문에 해당 지점+1부터 다시 값 계산
                idx = snake[idx] + 1
                continue
        # 뱀 도착점에 값이 없을 경우
        else:
            dp[snake[idx]] = turn
    else:
        dp[idx] = turn
    idx += 1
print(dp[-1])