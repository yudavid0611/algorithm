import sys
import heapq
from collections import defaultdict
sys.stdin = open('1167_input.txt')
input = sys.stdin.readline

## 입력 처리 ##
V = int(input().rstrip())

graph = defaultdict(list)

for _ in range(V):
    temp = list(map(int, input().split()))
    node1 = temp[0]
    
    for i in range(1, len(temp) - 1, 2):
        node2 = temp[i]
        dist = temp[i + 1]
        
        graph[node1].append([node2, dist])


## 최대 거리 구하기 ##
visited = [0] * (V + 1)
answer = 0

def postorder(node, dist):
    global answer, visited
    
    visited[node] = 1
    
    # leaf에서 자식노드까지 거리 저장
    dist_all = []
    for child, child_dist in graph[node]:
        if visited[child] == 0:
            now_dist = postorder(child, child_dist)
            heapq.heappush(dist_all, -now_dist)
    
    # leaf 노드일 경우
    if not dist_all:
        return dist
    
    else:
        d1 = 0
        d2 = 0

        # 자식 노드가 1개일 경우
        if len(dist_all) == 1:
            d1 = -dist_all[0]
        
        else:
            d1 = -heapq.heappop(dist_all)    
            d2 = -heapq.heappop(dist_all)    

    # 현재 노드에서 가질 수 있는 최대 길이
    now_max_dist = d1 + d2
    if now_max_dist > answer:
        answer = now_max_dist
    
    return d1 + dist

postorder(1, 0)
print(answer)