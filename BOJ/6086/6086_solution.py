import sys
from collections import defaultdict, deque
sys.stdin = open('6086_input.txt')
input = sys.stdin.readline


# Z까지의 경로 찾기
def bfs():
    q = deque()
    visited = defaultdict(str)
    q.append('A')
    visited['A'] = 'start'
    while q:
        node = q.popleft()
        for next_node in graph[node]:
            
            # 아직 방문하지 않았고, 물이 더 흐를 수 있는 경우
            if not visited[next_node] and capacity[node][next_node] - flow[node][next_node]:
                visited[next_node] = node
                if next_node == 'Z':
                    break
                q.append(next_node)
    return visited


# 최대 유량 찾기
def max_flow():
    answer = 0
    while True:
        route = bfs()

        # 더 이상 경로가 없을 경우
        if not route['Z']:
            return answer

        temp_flow = 1001

        # 경로에서 흐를 수 있는 최대 유량 찾기
        node = 'Z'
        while node != 'A':
            temp_flow = min(temp_flow, capacity[route[node]][node] - flow[route[node]][node])
            node = route[node]
        
        # 최대 유량만큼 뺴주기
        node = 'Z'
        while node != 'A':
            flow[route[node]][node] += temp_flow
            flow[node][route[node]] -= temp_flow
            node = route[node]

        answer += temp_flow

if __name__ == '__main__':
    N = int(input().rstrip())
    graph = defaultdict(list)

    # 용량
    capacity = defaultdict(dict)

    # 유량
    flow = defaultdict(dict)

    for _ in range(N):
        n1, n2, w = input().split()
        w = int(w)
        graph[n1].append(n2)
        graph[n2].append(n1)

        # 이미 추가된 경로일 경우
        if n2 in capacity[n1]:
            capacity[n1][n2] += w
            capacity[n2][n1] += w
        else:
            capacity[n1].update({n2: w})
            capacity[n2].update({n1: w})
            flow[n1].update({n2: 0})
            flow[n2].update({n1: 0})
    
    print(max_flow())