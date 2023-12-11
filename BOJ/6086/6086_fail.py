import sys
from collections import defaultdict, deque
sys.stdin = open('6086_input.txt')
input = sys.stdin.readline

N = int(input().rstrip())
graph = defaultdict(list)
for _ in range(N):
    n1, n2, w = input().split()
    w = int(w)
    graph[n1].append([n2, w])
    graph[n2].append([n1, w])

flow = defaultdict(int)

q = deque()
q.append(['A', 1001])
while q:
    n, w = q.popleft()
    if n == 'Z':
        flow['Z'] += w
    else:

        # 병렬 관계
        if flow[n] != 0:
            flow[n] += w
        else:
            flow[n] = w

        for n2, w2 in graph[n]:
            if flow[n2] == 0:
                q.append([n2, min(flow[n], w2)])

print(flow['Z'])