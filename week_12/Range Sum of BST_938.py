'''
### 938. Range Sum of BST
---
이진 검색 트리의 루트 노드가 주어지면 [low, high] 범위의 값을 가진 모든 노드 값의 합계를 반환합니다.

- [low, high] 범위에서 low, high 모두 포함해서 합계를 구해야 합니다. 
  ex) low= 10, high=15 일 경우 10 이상 15 이하의 합계를 구하면 됩니다.
  '''

  # Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 192ms
#  BST로  탐색을 실행하고,L과  R의 범위를 맞추면서 범위안에 노드만 살리고 
#  현재 노드가 해당 범위에 맞으면 합산을 진행한다. 
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack, sum = [root], 0
        while stack : 
            node = stack.pop()
            if node : 
                if node.val > L:  # L 보다 큰 경우 해당 node에서 left 방향으로 자른다.
                    stack.append(node.left)
                if node.val < R :   # R보다 작은 해당 node에서 right 방향으로 자른다.
                    stack.append(node.right)  

                # 현재 노드보다 크거나 작은경우의 처리를 위에서 다 진행했으니
                # 현재 노드가 [low, high] 범위안에 들어가는 체크하고 
                # 범위 안에 포함되면 합을 구한다.
                if L <= node.val <= R:  
                    sum += node.val
                    
        return sum


#  dfs(node.left)를 먼저해서 왼쪽 끝 까지 탐색 후 오른쪽 끝으로 탐색을 한다.
# 전체를 순회한 후 조건 (low<= node <= high ) 맞는 경우만 연산을 한다.

# 252ms

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        res = 0 
        def dfs(node): 
            nonlocal res
            if not node: return None 

            dfs(node.left)  # 왼쪽 부터 재귀 시작
            dfs(node.right)
            #print("node.val", node.val)
            if  low <= node.val <= high :
                res += node.val

        dfs(root)
        return res

#  범위 전체를 탐색해야 하므로 위의 코드가 dfs보다 더 시간이 오래 걸린다.

#  책에 있는 코드 [DFS 가지치기]
# return으로 해당 범위에 속하지 않는 경우 해당하는 범위로 보내기 위해 
#  해당 범위에 반대로 보낸다.   
#  ex) low보다 작은 경우 node.right로 더 큰 값을 탐색하게 만든다.

# 212 ms
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node): 
            if not node: return 0 
            
            if node.val < low :
                return dfs(node.right)
            elif node.val > high : 
                return dfs(node.left)
            return node.val + dfs(node.left) + dfs(node.right)
        
        return dfs(root)

'''
DFS로 범위 밖에 둔 값을 가지치기 하는 코드보다 stack 구조를 이용해 while 안에서 pop으로 필요한 node를 구하는 코드가 더 빠른 속도를 가진다.  

- 아마도 연산의 개수가 while이 더 적기에 더 빠른 속도를 가질 수 있고 추가로, 
  while는 내부 범위만 체크하면 되지만, dfs()는 범위를 가지친 후 다시 내부를 탐색해야하기에 더 많은 시간이 걸린것 같습니다.  
  
  
- 그렇지만 공간 복잡도는 dfs가 더 좋습니다. 
   while의 경우 sum 변수와 stack  변수가 필요한데 반해 dfs는 다른 변수가 추가로 필요하지 않습니다. 
'''
