import sys
from collections import defaultdict
sys.stdin = open('5052_input.txt')

class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def startsWith(self, word):
        node = self.root

        flag = 0
        for w in word:
            # 이미 등록된 철자인 경우 flag + 1
            if w in node.children:
                flag += 1
            node = node.children[w]
        # word로 시작하는 단어가 있을 경우
        if flag == len(word):
            return 0
        return 1

T = int(input())

for _ in range(T):
    N = int(input())

    nums = [sys.stdin.readline().rstrip() for _ in range(N)]
    nums.sort(reverse=True)

    trie = Trie()
    for n in nums:
        result = trie.startsWith(n)
        if result == 0:
            print('NO')
            break
    else:
        print('YES')