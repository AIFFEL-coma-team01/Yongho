'''
## 226. Invert Binary Tree
---
이진 트리의 루트가 주어지면 트리를 반전하고 루트를 반환합니다.

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = deque([root])
        while stack :
            node = stack.pop()  # 부모 노드로부터 아래로 내려간다.
            if node :   # 노드가 존재하는 경우 왼쪽과 오른쪽의 값을 swap한다.
                node.left, node.right = node.right, node.left 
                stack.extend([node.right, node.left])         # swap이 완료된 경우 stack에 다시 추가하여 해당 노드의 아래 값이 있는지 찾아간다.
        return root


root = [4,2,7,1,3,6,9]   # [4,7,2,9,6,3,1]
res = Solution.invertTree(0, root)
print(res)