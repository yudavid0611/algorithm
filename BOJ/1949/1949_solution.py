import sys
from collections import defaultdict
sys.setrecursionlimit(10000000)
sys.stdin = open('1949_input.txt')
input = sys.stdin.readline

N = int(input().rstrip())
population = [0] + list(map(int, input().split()))

tree = defaultdict(list)
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dp = [[0, 0] for _ in range(N + 1)]
visited = [0] * (N + 1)
def dfs(v):
    visited[v] = 1
    dp[v][1] = population[v]

    for u in tree[v]:
        if visited[u] == 0:
            dfs(u)
            
            # 자식 정점이 일반 마을일 경우의 누적 인구수를 가져올 수 있는 이유:
            # 일반 마을일 경우의 누적 인구수가 연속으로 세 번 이상 더 클 수 없음 
            dp[v][0] += max(dp[u][0], dp[u][1])
            dp[v][1] += dp[u][0]

dfs(1)
print(max(dp[1]))