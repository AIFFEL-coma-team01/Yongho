'''
### 104. Maximum Depth of Binary Tree
___

이진 트리의 루트가 주어지면 최대 깊이를 반환합니다. 
바이너리 트리의 최대 깊이는 루트 노드에서 가장 먼 리프 노드까지 가장 긴 경로에있는 노드 수입니다.


가장 깊게 들어갈 수 있는 node를 찾고 해당 node 까지 걸린 거리를 반환하면 된다. 

1-1. node와 depth를 인수로 받는 dfs 함수를 선언하고 node에 left, right 방향에 값이 있는 경우 (left를 먼저 탐색한다. left -> right)
   해당 방향으로 계속 탐색을 들어간다. 
1-2. 탐색을 하면서, 얼마나 깊은지 depth에 대한 정보도 줘야 하기에 Paremeter depth에다 +1을 한 값을 인수로 dfs를 재귀 호출 한다.

2. 해당 방향에 끝까지 가는 경우 return해서 현재 방향에 최종 길이를 max_depth 리스트에 append해서 모든 노드의 깊이를 구한다.

3. 모든 노드의 길이를 구한 후 그 길이중 가장 큰 값을 return 한다.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 40 ms
# 
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = [root]
        max_depth =[]
        depth = 0 

        def dfs(node, depth):
            if not node : 
                return
            if node.left :
                dfs(node.left, depth+1)
            if node.right :
                dfs(node.right, depth+1)
            return max_depth.append(depth)
        
        dfs(stack, 0)
        return max(max_depth)



# 48ms
# 위에 코드에서 max 구하는 부분을 heap으로 대체해서 사용한 코드
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        max_depth = []
        if not root : return 0
        def dfs(node, depth):
            if not node : 
                return 
            if node.left :
                dfs(node.left, depth+1)
            if node.right :
                dfs(node.right, depth+1)
            return heapq.heappush(max_depth, (-1*depth, depth))
        
        dfs(root, 1)
        return max_depth[0][1]  # 최대 힙 return

root = [3,9,20,None,None,15,7]  # 3
res = Solution.maxDepth(0, root)
print(res)