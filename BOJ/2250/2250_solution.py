import sys
from collections import defaultdict
sys.setrecursionlimit(10000000)
sys.stdin = open('2250_input.txt')
input = sys.stdin.readline

# 중위순회
def inorder(n, level, n_opposite):
    n_left_subtree = 0
    n_right_subtree = 0

    # 왼쪽 서브트리 순회
    if tree[n][0] != -1:
        n_left_subtree = inorder(tree[n][0], level + 1, n_opposite)
    
    # 현재 노드의 칼럼
    now_col = n_left_subtree + n_opposite + 1
    
    # 현재 level에 저장된 값이 없을 경우
    if left_col[level] == 0:
        left_col[level] = now_col
    
    # 현재 level에 저장된 값이 있을 경우
    else:
        # 최대 너비 업데이트
        if now_col - left_col[level] + 1 > answer[1]:
            answer[0], answer[1] = level, now_col - left_col[level] + 1
        elif now_col - left_col[level] + 1 == answer[1] and level < answer[0]:
            answer[0], answer[1] = level, now_col - left_col[level] + 1

    # 오른쪽 서브트리 순회
    if tree[n][1] != -1:
        n_right_subtree = inorder(tree[n][1], level + 1, now_col)

    return n_right_subtree + n_left_subtree + 1

if __name__ == '__main__':
    N = int(input().rstrip())
    tree = defaultdict(list)
    left_col = defaultdict(int)
    find_root = set([i for i in range(1, N + 1)])
    for i in range(1, N + 1):
        p, c_left, c_right = map(int, input().split())
        tree[p].append(c_left)
        tree[p].append(c_right)
        if c_left in find_root:
            find_root.remove(c_left)
        if c_right in find_root:
            find_root.remove(c_right)
        
    root = find_root.pop()
    answer = [1, 1]
    
    inorder(root, 1, 0)

    print(f'{answer[0]} {answer[1]}')