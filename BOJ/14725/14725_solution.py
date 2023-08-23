import sys
from collections import defaultdict
sys.stdin = open('14725_input.txt')
input = sys.stdin.readline

N = int(input())

class TrieNode:
    def __init__(self):
        self.children = defaultdict()
        # dfs 시 방문 여부를 체크할 변수
        self.visited = False

class Trie:
    def __init__(self):
        self.head = TrieNode()
    
    # 단어 삽입
    def insert(self, word):
        node = self.head

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
    
    # 결과 출력
    def print_answer(self):
        node = self.head
        self.dfs(node, 0)
    
    # children 탐색
    def dfs(self, n, depth):
        # 방문 처리
        n.visited = True

        # children이 있을 경우
        if n.children:
            # 사전 오름차순 정렬
            children = sorted(n.children.keys())

            for child in children:
                # 아직 방문하지 않은 노드일 경우
                if not n.children[child].visited:
                    # 먹이 print
                    if depth == 0:
                        print(f'{child}')
                    else:
                        print(f'{"--" * depth}{child}')

                    self.dfs(n.children[child], depth + 1)

trie = Trie()
for _ in range(N):
    k, *meals = input().split()
    trie.insert(meals)

trie.print_answer()