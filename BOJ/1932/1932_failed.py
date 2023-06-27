import sys
sys.stdin = open('1932_input.txt')

## 접근법 ##
# 1. Node 클래스 정의
# 2. input 받아서 Tree 구성하기
# 3. 트리 순회 함수 정의
# 4. 트리 순회하며 리프노드 도달 시 최대값 업데이트

## 결과: 메모리 초과 ##


# Node 클래스
class Tree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


# 전위순회
def preorder(n, row, col, agg):
    global max_value
    agg += n.value

    # print(agg)
    if row == N-1:
        if agg > max_value:
            max_value = agg
    else:
        n.left = Tree(value=node_dict[row+1][col])
        preorder(n.left, row+1, col, agg)
    
        n.right = Tree(value=node_dict[row+1][col+1])
        preorder(n.right, row+1, col+1, agg)


N = int(input())

node_dict = {}
for i in range(N):
    node_dict[i] = list(map(int, input().split()))

max_value = 0

node = Tree(node_dict[0][0])

preorder(node, 0, 0, 0)

print(max_value)