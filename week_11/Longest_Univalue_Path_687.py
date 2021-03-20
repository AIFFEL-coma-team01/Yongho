'''
## 687. Longest Univalue Path
---
이진 트리의 루트가 주어지면 경로의 각 노드가 동일한 값을 갖는 가장 긴 경로의 길이를 반환합니다. 
이 경로는 루트를 통과하거나 통과하지 않을 수 있습니다. 
두 노드 사이의 경로 길이는 노드 사이의 가장자리 수로 표시됩니다.

================================================================================================

543번과 비슷하게 dfs로 root를 받고 node.left, node.right로 탐색을 해나간다.  

1-1. node에서 left 값이 존재하는 경우 [자식 노드가 왼쪽에 있는 경우]
  - 현재 node에 val과 다음 노드(자식 노드)의 val이 일치하는지 확인하고 일치하면 node_left에 +1 
     일치하지 않는다면, 탐색할 이유가 없고 '동일한 값을 갖는 경로'가 끊겨야 하니 node_left를 
     0으로 만들어 준다. 

1-2. node에서 right 값이 존재하는 경우 [자식 노드가 오른쪽에 있는 경우]
    - 방향만 다를 뿐 1-1과 동일한 내용이다.

2. 가장 긴 경로를 반환해야하니 node_left, node_right에 max를 결과 값인(res)와 비교해서 저장해준다.

3.  node_left가 더 큰경우 node_left로 return,  node_right가 더 큰경우 node_right로 리턴해서 
    가장 긴 경로로 가게 return 해준다.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 356 ms ms
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        res =0
        def dfs(node) :
            nonlocal res
            if not node  :
                return 0
            
            node_left = dfs(node.left)
            node_right = dfs(node.right)
            
            if node.left :
                if node.left.val == node.val : 
                    node_left +=1
                else : 
                    node_left =0
            if node.right:
                if node.right.val == node.val :
                    node_right += 1
                else : 
                    node_right = 0
            res = max( res, node_left+node_right)
            if node_left > node_right :
                return node_left
            return node_right
            
        dfs(root)
        
        return root

root = [5,4,5,1,1,5]  # 2
res = Solution.maxDepth(0, root) 
print(res)
