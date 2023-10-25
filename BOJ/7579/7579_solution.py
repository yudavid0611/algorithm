import sys
sys.stdin = open('7579_input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
memories = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))

dp = [[0] * (100 * N + 1) for _ in range(N + 1)]

answer = 100 * 1e6
for app in range(1, N + 1):
    for cost_limit in range(0, 100 * N + 1):
        # 현재 앱의 cost <= cost_limit
        if costs[app] <= cost_limit:

            # 현재 앱 메모리 + 같이 처리할 수 있는 메모리 최대값 vs 이전 앱에서의 최대값
            dp[app][cost_limit] = max(dp[app - 1][cost_limit - costs[app]] + memories[app], dp[app - 1][cost_limit])
        
        # 현재 앱의 cost > cost_limit
        else:
            dp[app][cost_limit] = dp[app - 1][cost_limit]
        
for cost in range(100 * N + 1):
    if dp[-1][cost] >= M:
        print(cost)
        break