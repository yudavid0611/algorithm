# 12865: 평범한 배낭

import sys
sys.stdin = open('12865_input.txt')

N, K = map(int, input().split())

# dp[a][b]: a개의 물품을 담을 때, b 무게에서의 최대 가치
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    # w: 현재 물품의 무게 / v: 현재 물품의 가치
    w, v = map(int, input().split())

    # 무게 1부터 k까지 순회
    for j in range(1, K + 1):
        # 현재 물품을 넣을 수 없는 경우 -> dp[i-1][j]가 무게 j에서 가질 수 있는 최대 가치
        if w > j:
            dp[i][j] = dp[i-1][j]
        else:
            # 현재 물품을 포함하느냐 마느냐를 결정
            dp[i][j] = max(v + dp[i-1][j-w], dp[i-1][j])

print(dp[N][K])