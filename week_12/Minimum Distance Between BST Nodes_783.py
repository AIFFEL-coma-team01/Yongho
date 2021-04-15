'''
### 783. Minimum Distance Between BST Nodes
---
이진 검색 트리 (BST)의 루트가 주어지면 트리에있는 두 개의 서로 다른 노드 값 간의 최소 차이를 반환합니다.  

**참고** :이 질문은 530번과 동일합니다.

조건 :
0 <= Node.val <= 10^5
=============================================================================

Input : [4,2,6,1,3]

node.val :  6    right :  100001
node.val :  4    right :  6
node.val :  3    right :  4
node.val :  2    right :  3
node.val :  1    right :  2

-> 이진 트리는 오른쪽에 있는 값이 왼쪽에 있는 값보다 작은 값이므로, 
   오른쪽->왼쪽으로 노드의 차이를 구한다.

시작 부분에 있는 오른쪽 노드의 경우 보다 큰 값을 넣어야 양수가 되고 
다음 진행에서 원래의 노드의 [오른쪽-왼쪽] 계산이 이루어 지므로 
10^5 보다 1이 더 큰 값을 넣어준다.

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 24ms

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        res =100001
        _right = 100001
        def dfs(node) :
            nonlocal res,_right
            if node : 
                dfs(node.right)
                #print("node.val : ", node.val,"   right : ", _right)
                res = min(res, _right - node.val )
                _right = node.val
                dfs(node.left)

        dfs(root)