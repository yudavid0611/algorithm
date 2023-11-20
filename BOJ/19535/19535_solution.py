import sys
from collections import defaultdict
sys.setrecursionlimit(10000000)
sys.stdin = open('19535_input.txt')
input = sys.stdin.readline

# nC3 구하기
def num_comb(n, m=3):
    if n < m:
        return 0
    numerator = 1
    denominator = 1
    for i in range(n, n - m, -1):
        numerator *= i
    for j in range(1, m + 1):
        denominator *= j
    return int(numerator / denominator)

# 트리 순회
def dfs(v, p):
    global n_case1, n_case2

    visited[v] = 1

    # ㄷ 체크
    n_case1 += (len(graph[v]) - 1) * (len(graph[p]) - 1)

    # ㅈ 체크
    n_case2 += num_comb(len(graph[v]))
    
    for c in graph[v]:
        if visited[c] == 0:
            dfs(c, v)

if __name__ == '__main__':
    N = int(input().rstrip())
    graph = defaultdict(list)
    for _ in range(N - 1):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    # ㄷ 개수
    n_case1 = 0

    # ㅈ 개수
    n_case2 = 0

    # 방문 표시
    visited = [0] * (N + 1)

    # dfs 인자로 p를 넣어줘야 하기 때문에
    # 정점 0을 가상으로 넣어줌
    graph[0].append(0)

    dfs(1, 0)

    # DUDUDUNGA
    if n_case1 == n_case2 * 3:
        print('DUDUDUNGA')
    # D
    elif n_case1 > n_case2 * 3:
        print('D')
    # G
    else:
        print('G')