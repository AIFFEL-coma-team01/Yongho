'''
## 트라이(Trie)
**트라이(Trie)**는 검색 트리의 일종으로 일반적으로 키가 문자열인, 동적 배열 또는 연관 배열을 저장하는 데 사용되는 정렬된 트리 자료구조다.

- 트라이(Trie)는 실무에 매우 유용하게 쓰이는 자료구조로서, 특히 자연어 처리(NLP) 분야에서 문자열 탐색을 위한 자료구조로 널리 쓰인다.  

# 트라이 개념이 헷갈려서 정의를 적었습니다. 


### 336. Palindrome Pairs
---
고유 한 단어 목록이 주어지면 주어진 목록에있는 고유 한 색인 (i, j) 쌍을 모두 반환하여 
두 단어 단어 [i] + 단어 [j]의 연결이 회문이되도록합니다.


'''

# 1004ms
import collections

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word[::] == word [::-1]
    
    #단어 삽입 메소드
    def insert(self, index, word) -> None:
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[0:len(word) - i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
            node.val = char
        node.word_id = index

    def search(self, index, word) -> List[List[int]]:
        result = []
        node = self.root
        while word:
            # 판별 로직
            if node.word_id >= 0:
                if self.is_palindrome(word): 
                    result.append([index,node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]
        
        # 판별 로직 
        if node.word_id >= 0 and node.word_id != index:
            result.append([index,node.word_id])
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])  
        return result

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        for i, word in enumerate(words):
            trie.insert(i,word)
        
        results = []  
        for i, word in enumerate(words):
            results.extend(trie.search(i,word))

        return results