import sys
sys.stdin = open('strategy/graph_search/1219_input.txt', 'r')

def adjlist(vertex_num, edge_num):                              # 인접행렬 리스트를 반환하는 함수
    edges = list(map(int, input().split()))                     # 간선 정보 리스트로 형변환
    arr = [[0] * (vertex_num) for _ in range(vertex_num)]       # 정점 개수만큼의 행과 열을 갖는 2차원 리스트 생성
    for i in range(edge_num):
        n1, n2 = edges[i*2], edges[i*2+1]
        arr[n1][n2] = 1
    return arr

def dfs(v, arr, vertex_num):                                    # dfs 함수
    root = []                                                   # 루트를 저장할 리스트 생성
    visited = [0] * (vertex_num)                                # 방문한 정점를 표시할 리스트 생성
    stack = [0] * (vertex_num)                                  # 이전 경로를 저장해둘 스택 생성
    top = -1
    
    visited[v] = 1
    root.append(v)
    while True:
        for idx, w in enumerate(arr[v]):
            if w == 1 and visited[idx] == 0:                    # 길이 존재하고, 방문한 적이 없는 경우
                top += 1
                stack[top] = v                                  # 스택에 현재 정점 추가
                v = idx                                         # idx 정점로 이동
                root.append(v)                                  # root에 정점 추가
                visited[v] = 1                                  # 방문 기록 남기기
                break
        else:
            if top != -1:                                       # 스택에 정점가 남아 있을 경우
                v = stack[top]                                  # 이전 정점로 이동
                stack[top] = 0                                  # top 정점 초기화
                top -= 1
            else:
                break
    return root


for _ in range(1, 11):
    vertex_num = 100                                            # 정점 개수는 100
    t, edge_num = map(int, input().split())                     # 테스트케이스 넘버와 간선 개수 받기
    arr = adjlist(vertex_num, edge_num)                         # adjlist 함수를 통해 인접행렬 반환 받기
    root = dfs(0, arr, vertex_num)                              # dfs 함수를 통해 root 반환 받기
    if 99 in root:                                              # 99가 root 안에 있을 경우 1 출력 / 없을 경우 0 출력
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')