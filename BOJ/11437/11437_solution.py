import sys
from math import log2
from collections import defaultdict
sys.stdin = open('11437_input.txt')
sys.setrecursionlimit(int(1e5))

input = sys.stdin.readline

N = int(input())

# 트리가 가질 수 있는 최대 깊이 구하기
# 사실 최대 깊이보다 클 수 있다.
max_depth = int(log2(50000)) + 1

# 방문 표시
visited = [0] * (N + 1)

# 깊이
depth = [0] * (N + 1)

# 부모 저장
parent = [[0] * (max_depth + 1) for _ in range(N + 1)]

graph = defaultdict(list)

for _ in range(N - 1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)


# 각 노드의 깊이 및 첫 번째 부모 구하기
def dfs(n, d):
    global visited, depth
    visited[n] = 1
    depth[n] = d

    for c in graph[n]:
        if not visited[c]:
            # 바로 위 부모 저장
            parent[c][0] = n
            dfs(c, d + 1)


# 각 노드의 2^i번째 부모 구하기
def set_parent():
    dfs(1, 0)
    for i in range(1, max_depth + 1):
        for j in range(1, N + 1):
            parent[j][i] = parent[parent[j][i-1]][i-1]


# 최소 공통 조상 찾기
def lca(a, b):
    # b가 더 깊도록 만들기
    if depth[a] > depth[b]:
        a, b = b, a

    # 동일한 깊이로 만들기
    for i in range(max_depth - 1, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            b = parent[b][i]

    # a와 b가 동일할 경우
    if a == b:
        return a
    
    # 공통 조상 찾기
    for i in range(max_depth -1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
        
    return parent[a][0]

set_parent()

M = int(input())

for i in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))