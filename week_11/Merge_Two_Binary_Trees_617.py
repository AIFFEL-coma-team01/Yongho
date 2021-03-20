'''
### 617. Merge Two Binary Trees
---
두 개의 바이너리 트리 root1과 root2가 제공됩니다. 
그중 하나를 다른 쪽을 덮기 위해두면 두 트리의 일부 노드가 겹치는 반면 다른 노드는 겹치지 않는다고 상상해보십시오. 
두 트리를 새 이진 트리로 병합해야합니다. 
병합 규칙은 두 노드가 겹치는 경우 병합 된 노드의 새 값으로 노드 값을 합산하는 것입니다. 
그렇지 않으면 NOT null 노드가 새 트리의 노드로 사용됩니다. 병합 된 트리를 반환합니다. 

참고 : 병합 프로세스는 두 트리의 루트 노드에서 시작해야합니다.


두 트리를 받을 dfs 함수를 선언하고 두 트리에서 값이 있는 경우 lfet,right의 val을 각각 더하면서 재귀 호출한다.

1-1. dfs(node_1, node_2) 만든 후 node_1이 없으면 node_2가 있는지 확인 
1-2. node_2가 없으면 node_1이 있는지 확인한다. 

2. 위의 if 조건 모두를 통과한 겨우 node_1, node_2 모두 있다는 의미이다.  
   node_1을 기준으로 삼아 node_2의 val을 더해주면서 병합된 새로운 노드를 만든다.

'''

# 84ms
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:

        def dfs(node_1, node_2) : 
        
            if not node_1 : return node_2
            if not node_2 : return node_1
            
            node_1.val += node_2.val
            node_1.left = dfs(node_1.left, node_2.left)
            node_1.right = dfs(node_1.right, node_2.right)

            return node_1

        return dfs(root1, root2)
        