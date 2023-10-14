import sys
from math import log2, ceil
sys.setrecursionlimit(100000)
sys.stdin = open('2042_input.txt')
input = sys.stdin.readline

# 세그먼트 트리 초기화
def create_segtree(node, start, end):
    # leaf
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    
    else:
        mid = (start + end) // 2
        left_sum = create_segtree(node * 2, start, mid)
        right_sum = create_segtree(node * 2 + 1, mid + 1, end)
        total = left_sum + right_sum
        tree[node] = total
        return total

# 세그먼트 트리 업데이트
def update_segtree(node, start, end, idx, diff):
    if idx < start or idx > end:
        return
    
    tree[node] += diff
    
    if start != end:
        mid = (start + end) // 2
        update_segtree(node * 2, start, mid, idx, diff)
        update_segtree(node * 2 + 1, mid + 1, end, idx, diff)
    
# 구간 합 출력
def interval_sum(node, start, end, left, right):
    # 구간에 포함되지 않을 경우
    if right < start or left > end:
        return 0
    
    elif left <= start and end <= right:
        return tree[node]
        
    # 구간에 포함될 경우
    else:
        mid = (start + end) // 2
        left_sum = interval_sum(node * 2, start, mid, left, right)
        right_sum = interval_sum(node * 2 + 1, mid + 1, end, left, right)
        return left_sum + right_sum

if __name__ == '__main__':
    N, M, K = map(int, input().split())

    level = ceil(log2(N))
    leaf_start = 2 ** level
    tree = [0] * (2 ** (level + 1))
    nums = [int(input().rstrip()) for _ in range(N)]
    
    # 세그먼트 트리 초기화
    create_segtree(1, 0, N - 1)

    for _ in range(M + K):
        key, n1, n2 = map(int, input().split())

        # 수 변경
        if key == 1:
            diff = n2 - nums[n1 - 1]
            nums[n1 - 1] = n2
            update_segtree(1, 0, N - 1, n1 - 1, diff)
        
        # 구간 합 출력
        else:
            print(interval_sum(1, 0, N - 1, n1 - 1, n2 - 1))