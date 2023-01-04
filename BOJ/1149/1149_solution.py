# 1149: RGB거리

import sys
sys.stdin = open('1149_input.txt')

N = int(input())

costs = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N)]
dp[0] = costs[0][:]

for row in range(1, N):
    for col in range(3):
        dp[row][col] = min(dp[row - 1][(col + 1) % 3], dp[row - 1][(col + 2) % 3]) + costs[row][col]

print(min(dp[N-1]))