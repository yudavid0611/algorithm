import sys
from math import log2, ceil
sys.setrecursionlimit(1000000)
sys.stdin = open('28099_input.txt')
input = sys.stdin.readline

# segment 트리 만들기
def build(node, start, end):
    if start == end:
        seg_tree[node] = arr[start]
        return
    else:
        mid = (start + end) // 2
        build(node * 2, start, mid)
        build(node * 2 + 1, mid + 1, end)

        # 구간 최대값 저장하기
        seg_tree[node] = max(seg_tree[node * 2], seg_tree[node * 2 + 1])
        return

# 쿼리
def query(node, target, start, end, left, right):
    global is_weird

    # 구간을 벗어난 경우
    if right < start or end < left:
        return
    
    # 구간을 포함하고 있는 경우
    elif left <= start and end <= right:
        if seg_tree[node] > target:
            is_weird = False
        return
    
    # 구간을 일부 포함하고 있을 경우
    else:
        mid = (start + end) // 2
        query(node * 2, target, start, mid, left, right) 
        query(node * 2 + 1, target, mid + 1, end, left, right)
        return

if __name__ == '__main__':
    T = int(input().rstrip())
    for _ in range(T):
        N = int(input().rstrip())

        # 세그먼트 트리 height 구하기
        height = ceil(log2(N))

        # 세그먼트 트리 노드 개수 구하기
        n_nodes = 2 ** (height + 1) - 1

        # 세그먼트 트리
        seg_tree = [0] * (n_nodes + 1)
        arr = list(map(int, input().split()))

        # 세그먼트 트리 만들기
        build(1, 0, N - 1)

        # 최근 각 숫자가 나온 인덱스 저장
        num_index = [-1] * (N + 1)
        is_weird = True
        for i in range(N):
            # 처음 나온 숫자일 경우
            if num_index[arr[i]] == -1:
                num_index[arr[i]] = i               
            
            # 이전에 나온 숫자일 경우
            else:
                query(1, arr[i], 0, N - 1, num_index[arr[i]] + 1, i - 1)
                if not is_weird:
                    print('No')
                    break
                num_index[arr[i]] = i
        else:
            print('Yes')