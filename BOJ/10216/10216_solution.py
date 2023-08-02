import sys
from math import sqrt
sys.stdin = open('10216_input.txt')

# find 연산(경로 압축 적용)
def find_parent(n):
    if parent[n] == n:
        return n
    parent[n] = find_parent(parent[n])
    return parent[n]

# union 연산
def union_set(m, n):
    m_parent = find_parent(m)
    n_parent = find_parent(n)
    parent[n_parent] = m_parent

# 두 진영 사이 거리와 R의 합 비교
def distance(a, b):
    d = sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
    if a[2] + b[2] >= d:
        return True
    return False

T = int(input())

for _ in range(T):
    N = int(input())
    enemies = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
    # parent 초기화: 자기 자신을 부모로 지정
    parent = [i for i in range(N)]

    for i in range(N):
        for j in range(i, N):
            # 직접 통신이 가능할 경우
            if distance(enemies[i], enemies[j]):
                union_set(i, j)
    
    # 대표자를 넣을 집합
    representative = set()
    for i in range(N):
        p = find_parent(i)
        if p not in representative:
            representative.add(p)
    
    print(len(representative))