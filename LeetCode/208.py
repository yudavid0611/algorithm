class Trie:
    root = {}

    def __init__(self, is_root=True):
        # 단어 완성 여부를 나타냄
        self.word = False
        # 다음에 오는 단어 저장
        self.children = {}
        
        # 테스트 케이스마다 root를 초기화하기 위한 코드
        if is_root:
            Trie.root = {}
        

    def insert(self, word: str) -> None:
        node = Trie.root

        if word[0] not in node:
            node.update({word[0]: Trie(is_root=False)})
        
        node = node[word[0]]
        
        for char in word[1:]:
            # char가 저장되어 있지 않은 경우 children에 추가
            if char not in node.children:
                node.children.update({char: Trie(is_root=False)})
            node = node.children[char]
        
        # 단어 완성
        node.word = True
        

    def search(self, word: str) -> bool:
        node = Trie.root

        if word[0] not in node:
            return False

        node = node[word[0]]

        for char in word[1:]:
            if char not in node.children:
                return False
            node = node.children[char]
        
        # 단어가 존재하는 경우
        if node.word:
            return True
        # 단어가 존재하지 않을 경우
        else:
            return False
            
        
    def startsWith(self, prefix: str) -> bool:
        node = Trie.root

        print(node)
        if prefix[0] not in node:
            return False

        node = node[prefix[0]]

        for char in prefix[1:]:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)