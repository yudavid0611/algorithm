import sys
from collections import defaultdict
sys.setrecursionlimit(100000)
sys.stdin = open('4256_input.txt')
input = sys.stdin.readline

def postorder(node, node_idx, left_subtree, right_subtree):
    global answer

    # 왼쪽 서브트리 노드 개수가 1일 경우 -> 왼쪽 자식
    if len(left_subtree) == 1:
        answer += ' ' + left_subtree[0]
    
    # 왼쪽 서브트리 분할
    elif len(left_subtree) > 1:
        left_subtree_root = result_preorder[node_idx + 1]
        left_subtree_node_idx = left_subtree.index(left_subtree_root)
        postorder(left_subtree_root, node_idx+1, left_subtree[:left_subtree_node_idx], left_subtree[left_subtree_node_idx+1:])
    
    # 오른쪽 서브트리 노드 개수가 1일 경우 -> 오른쪽 자식
    if len(right_subtree) == 1:
        answer += ' ' + right_subtree[0]
    
    # 오른쪽 서브트리 분할
    elif len(right_subtree) > 1:
        right_subtree_root = result_preorder[node_idx + len(left_subtree) + 1]
        right_subtree_node_idx = right_subtree.index(right_subtree_root)
        postorder(right_subtree_root, node_idx+len(left_subtree)+1, right_subtree[:right_subtree_node_idx], right_subtree[right_subtree_node_idx+1:])
    
    answer += ' ' + node

if __name__ == '__main__':
    T = int(input().rstrip())

    for _ in range(T):
        N = int(input().rstrip())
        result_preorder = input().split()
        result_inorder = input().split()
        tree = defaultdict(list)
        root = result_preorder[0]
        root_idx = result_inorder.index(root)
        answer = ''
        postorder(root, 0, result_inorder[:root_idx], result_inorder[root_idx+1:])
        print(answer[1:])