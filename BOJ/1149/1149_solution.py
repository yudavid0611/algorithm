# 1149: RGB거리

# flow
# cost 이중 리스트/
# cost[n][m]의 값은 cost[n-1]에서 동일한 색깔을 제외한 값중 최소 값에 해당 위치의 값을 더한 값


import sys
sys.stdin = open('1149_input.txt')

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N)]

# 첫째 행은 costs 그대로
dp[0] = costs[0][:]

# 행 순회
for row in range(1, len(costs)):
    # 열 순회
    for col in range(len(3)):
        

        





