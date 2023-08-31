## 시간 초과 ##

import sys
from collections import defaultdict
sys.setrecursionlimit(10000)
sys.stdin = open('11437_input.txt')
input = sys.stdin.readline

N = int(input())
tree = defaultdict(list)
graph1 = defaultdict(list)
graph2 = defaultdict(list)

for _ in range(N - 1):
    n1, n2 = map(int, input().split())
    graph1[n1].append(n2)
    graph2[n2].append(n1)

graphs = [graph1, graph2]
visited = [0] * (N + 1)

def make_tree(n):
    global visited, tree

    for graph in graphs:
        for n2 in graph[n]:
            if visited[n2] == 0:
                visited[n2] = 1
                tree[n].append(n2)
                make_tree(n2)

visited[1] = 1
make_tree(1)


M = int(input())

def postorder(n):
    global lca, target
    
    count = 0
    for c in tree[n]:
        count += postorder(c)
    
    if n in target:
        count += 1

    if count == 2:
        lca = n
        return 0
    
    else:
        return count

for _ in range(M):
    target = list(map(int, input().split()))
    
    lca = None
    postorder(1)
    print(lca)