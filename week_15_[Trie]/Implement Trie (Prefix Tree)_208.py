'''
## 트라이(Trie)
트라이(Trie)는 검색 트리의 일종으로 일반적으로 키가 문자열인, 동적 배열 또는 연관 배열을 저장하는 데 사용되는 정렬된 트리 자료구조다.

- 트라이(Trie)는 실무에 매우 유용하게 쓰이는 자료구조로서, 특히 자연어 처리(NLP) 분야에서 문자열 탐색을 위한 자료구조로 널리 쓰인다.  

### 208. Implement Trie (Prefix Tree)

#trie ( "try"로 발음) 또는 접두사 트리는 문자열 데이터 세트에서 키를 효율적으로 저장하고 검색하는 데 사용되는 트리 데이터 구조입니다. 자동 완성 및 맞춤법 검사기와 같은이 데이터 구조의 다양한 응용 프로그램이 있습니다. 
Trie 클래스를 구현합니다. 
- `Trie ()` trie 객체를 초기화합니다. 
- `void insert (String word)` 문자열 단어를 trie에 삽입합니다. 
- `boolean search (String word)` 문자열 단어가 trie에 있으면 (즉, 이전에 삽입 된 경우) `true`를 반환하고 그렇지 않으면 `false`를 반환합니다. 
- `boolean startsWith (String prefix)` `접두사` 접두사가있는 이전에 삽입 된 문자열 `단어`가 있으면 `true`를 반환하고 그렇지 않으면 `false`를 반환합니다.

'''

class TrieNode:
    def __init__(self): 
        self.word = False
        self.child = collections.defaultdict(TrieNode)


# 196ms
class Trie:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for ch in word:
            node = node.child[ch]
        node.word = True

            

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for ch in word:
            if ch not in node.child : # 단어가 없는 경우
                return False
            node = node.child[ch]
        return node.word
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for ch in prefix:
            if ch not in node.child : # 단어가 없는 경우
                return False
            node = node.child[ch]
            
        return True
        
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)