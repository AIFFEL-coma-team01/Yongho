'''
## 543. Diameter of Binary Tree
---

이진 트리의 루트가 주어지면 트리 지름의 길이를 반환합니다. 
이진 트리의 지름은 트리의 두 노드 사이에서 가장 긴 경로의 길이입니다. 
이 경로는 루트를 통과하거나 통과하지 않을 수 있습니다. 
두 노드 사이의 경로 길이는 노드 사이의 가장자리 수로 표시됩니다.


1. dfs로 root를 받는다. 
2. dfs 내부 에서 해당 노드의 root_left, root_right를 부르면서 탐색을 시작한다. 
3. 재귀를 빠져나올때 한 단계당 그 만큼의 거리를 더해야하기 때문에 +1을 더해주고 
   최종 결과 값(res)과 현재 지름과의 최대 값을 구해준다.  
4. return으로 left와 right의 최대 길이를 줘서 가장 긴 경로를 구한다.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 48ms
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0
        def dfs(root) :
            nonlocal res
            if not root :
                return 0
            root_left = dfs(root.left)

            root_right = dfs(root.right)
            res = max(res , root_left + root_right +1)   
            # +1이 없는 경우 root.left + root.right는 0이외에 값이 나올 수 없다.  [+1의 의미는 경로가 더해진다는 것이다.] 

            return max(root_left, root_right)+1
        
        dfs(root)
        return res-1


root = [1,2,3,4,5]  # 3
res = Solution.maxDepth(0, root)
print(res)
