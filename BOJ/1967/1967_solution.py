import sys
from collections import defaultdict
sys.stdin = open('1967_input.txt')
sys.setrecursionlimit(100000)

# 중위 순회
def inorder(n, w, tree, weight_agg):
    # leaf일 경우
    if not tree[n]:
        return w
    else:
        weights = []
        # 자식 노드 순회
        for child in tree[n]:
            weights.append(inorder(child[0], child[1], tree, weight_agg))
        
        weights.sort(reverse=True)
        # 상위 2개 노드 합 기록
        weight_agg[n] = sum(weights[:2])
        return weights[0] + w

n = int(input())

tree = defaultdict(list)
for _ in range(n - 1):
    p, c, e = map(int, sys.stdin.readline().split())
    tree[p].append([c, e])

weight_agg = [0] * (n + 1)

inorder(1, 0, tree, weight_agg)
print(max(weight_agg))