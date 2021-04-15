'''
### 1038. Binary Search Tree to Greater Sum Tree
---

이진 검색 트리 (BST)의 루트가 주어지면 원래 BST의 모든 키가 원래 키와 BST의 원래 키보다 큰 모든 키의 합계로 변경되도록 더 큰 트리로 변환합니다.   

*다시 말해 이진 검색 트리는 다음 제약 조건을 충족하는 트리입니다.*

- 노드의 왼쪽 하위 트리에는 노드의 키보다 작은 키가있는 노드 만 포함됩니다. 
- 노드의 오른쪽 하위 트리에는 노드의 키보다 큰 키가있는 노드 만 포함됩니다. 
- 왼쪽 및 오른쪽 하위 트리도 모두 이진 검색 트리 여야합니다.


================================================================

위의 제약조건에서 오른쪽 하위 트리는 자기 자신보다 큰 노드만 있다고 했기에, 
오른쪽 부터 왼쪽으로 누적 순회를 하면 된다.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#  순서를 오른쪽 -> 왼쪽 순으로 dfs 돌게 만든다.

# 24ms
# solution_1 중위 순회
class Solution:
    val: int =0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 중위 순회 노드 값 누적
        if root: 
            self.bstToGst(root.right)
            self.val += root.val 
            root.val = self.val
            self.bstToGst(root.left)

        return root

# 28ms 
# solution_2 dfs
# dfs 함수를 만든 후 재귀 호출
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        accum = 0
        def dfs(node) : 
            if not node  : return None

            nonlocal accum               
            dfs(node.right)
            node.val += accum
            accum = node.val
            dfs(node.left)
            

        dfs(root)

        return root

# self 를 불러서 bstToGst 함수를 직접 재귀 호출
# 24ms
class Solution:
    accum =0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root : return None
        self.bstToGst(root.right)
        root.val += self.accum
        self.accum = root.val
        self.bstToGst(root.left)
        return root