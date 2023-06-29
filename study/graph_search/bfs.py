import sys
from collections import deque                                       # queue를 deque 클래스로 구현
sys.stdin = open('strategy/graph_search/1219_input.txt', 'r')

def adjlist(vertex_num, edge_num):                                  # 인접행렬 리스트를 반환하는 함수
    edges = list(map(int, input().split()))                         # 간선 정보 리스트로 형변환
    arr = [[0] * (vertex_num) for _ in range(vertex_num)]           # 정점 개수만큼의 행과 열을 갖는 2차원 리스트 생성
    for i in range(edge_num):
        n1, n2 = edges[i*2], edges[i*2+1]
        arr[n1][n2] = 1
    return arr

def bfs(v, arr, vertex_num):                                        # bfs 함수 정의     
    visited = [0] * (vertex_num)                                    # 정점의 방문 여부를 표시할 리스트(방문x->0, 방문o->1)
    queue = deque()                                                 # queue
    
    visited[v] = 1          

    while True:
        for idx, w in enumerate(arr[v]):                            # v 정점에 연결된 자식 정점들 중 아직 방문하지 않은 정점일 경우 queue에 추가
            if w == 1 and visited[idx] == 0:
                queue.append(idx)

        if len(queue) == 0:                                         # queue에 더 이상 원소가 없으면 break
            break
        else:                                                       # queue에 원소가 있을 경우
            v = queue.popleft()                                     # 맨 앞에 있는 queue의 원소 정점으로 이동
            visited[v] = 1

    return visited


for _ in range(1, 11):
    vertex_num = 100                     
    t, edge_num = map(int, input().split())     
    arr = adjlist(vertex_num, edge_num)                 
    visited = bfs(0, arr, vertex_num)                  
    if visited[99] == 1:                                            # 99 노드의 값이 1인 경우 1 출력, 0인 경우 0 출력                                   
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')