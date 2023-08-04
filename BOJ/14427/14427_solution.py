import sys
import math
sys.stdin = open('14427_input.txt')
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())

# leaf 노드 개수
leaf_num = math.ceil(math.log2(N))

# tree의 모든 노드
nodes = [[0, 1000000001] for _ in range(2 **(leaf_num + 1) - 1)]

# leaf 노드의 시작 인덱스
leaf_start = 2 ** leaf_num - 1

# leaf 초기화
for idx, n in enumerate(nums):
    nodes[idx + leaf_start] = [idx + 1, n]

# 쿼리 요청에 따른 leaf 및 부모 노드의 값 업데이트 함수
def update(node, v, leaf_start):
    # 현재 노드 인덱스
    now_node = node + leaf_start
    # 쿼리 요청에 따른 값 수정
    nodes[now_node][1] = v

    while now_node != 0:
        # 부모 노드 인덱스
        now_node = (now_node - 1) // 2
        left, right = nodes[2 * now_node + 1], nodes[2 * now_node + 2]
        if left[1] <= right[1]:
            nodes[now_node] = [left[0], left[1]]
        else:
            nodes[now_node] = [right[0], right[1]]

# 초기 leaf 노드에 따른 부모 노드 값 업데이트
for idx, n in enumerate(nums):
    update(idx, n, leaf_start)
    
for _ in range(M):
    q = input().split()

    if len(q) == 1:
        print(nodes[0][0])
    else:
        _, i, v = map(int, q)
        update(i - 1, v, leaf_start)