import sys
sys.stdin = open('11812_input.txt')
input = sys.stdin.readline

# 노드의 레벨 찾기
def find_level(n, k):
    if n == 1:
        return 1
    
    level = 1
    last_node = 1
    while True:
        next_last_node = last_node * k + 1
        if next_last_node >= n:
            level += 1
            break
        level += 1
        last_node = next_last_node
    return level

# 부모 노드 찾기
def find_parent(n, k):
    q, r = divmod(n, k)

    # 나머지가 0 또는 1인 경우 몫이 곧 부모 노드
    if r == 0 or r == 1:
        return q
    else:
        return q + 1

# 최소 공통 조상 찾기
def lca(n, m, k):
    n_level = find_level(n, k)
    m_level = find_level(m, k)

    # n의 level이 더 크도록
    if n_level < m_level:
        n, m, n_level, m_level = m, n, m_level, n_level
    
    # 노드 사이 거리
    dist = 0

    # level 맞추기(n 노드 level을 m 노드 레벨로 맞추기)
    while n_level > m_level:
        n = find_parent(n, k)
        n_level -= 1
        dist += 1

    # 공통 조상 찾기
    while n != m:
        n = find_parent(n, k)
        m = find_parent(m, k)
        dist += 2

    return dist

if __name__ == '__main__':
    N, K, Q = map(int, input().split())
    
    for _ in range(Q):
        n, m = map(int, input().split())
        
        # K가 1인 경우 두 수의 차가 곧 최소 거리
        if K == 1:
            print(abs(m - n))
        else:
            print(lca(n ,m, K))