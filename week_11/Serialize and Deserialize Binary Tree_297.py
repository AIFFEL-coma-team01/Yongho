'''
## 297. Serialize and Deserialize Binary Tree

---

직렬화는 데이터 구조 또는 개체를 일련의 비트로 변환하여 파일 또는 메모리 버퍼에 저장하거나 
네트워크 연결 링크를 통해 전송하여 나중에 동일한 또는 다른 컴퓨터 환경에서 재구성하는 프로세스입니다. 
이진 트리를 직렬화 및 역 직렬화하는 알고리즘을 설계합니다. 직렬화 방법에는 제한이 없습니다.

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque



# 104 ms

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res =[]   # node를 돌면서 res에 문자열 형태로 저장한다.
        def dfs(node):
            nonlocal res
            if node:   # 현재 node에 값을 str()을 사용해 문자열로 바꾼 후 res에 저장한다.
                res.append(str(node.val))

                # 현재 node의 값을 문자열로 저장한 후에는 다음 노드를 알아야 하니 left 부터 recursive를 진행한다.
                #  왼쪽 부터  탐색을 시작해서 오른쪽으로 향하게 한다.
                dfs(node.left)           
                dfs(node.right) 
            else :
                res.append('null')  # node의 갚이 None인 경우 res에 null 값을 넣어 준다. 
            return None
        dfs(root)
#        print(' '.join(res))
        return ' '.join(res)   # 리스트인 res를 하나의 문자열로 반환해야하니 join()을 사용하고 
                                # deserialize() 할 때를 위해 ' '리스트 인덱스 기준으로 공백으로 분리를 시킨 후 join 한다.
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        tree = data.split(' ')  # serialize()에서 ' '  공백을 기준으로 문자열을 분리해 return 했기에 split(' ')을 사용할 수 있다.
        iter_node = iter(tree)  # 인덱스 단위로 다음 값을 호출할 수 있게 하기 위해 iter()로 iterable 객체인 list가
                                # iterator를 반환하고 iterator에서 next를 사용해 인덱스 단위 즉 'node' 단위로 값을 꺼낼 수 있게 만든다.
        
        def re_tree(iter_node):  # iter_node는 iterator 객체이다.
            next_node = next(iter_node)  # iterator 객체 이기에 next로 다음 값을 꺼낼 수 있다. [ 여기선 다음 노드의 의미이다. ]
            if next_node == 'null' :  # 다음 노드가' null'인 경우 위에서 None인 경우에 'null'로 저장 했기엔 다시 'None'로 return 해준다.
                return None


            cur = TreeNode(int(next_node))  # root 노드 부터 다시 TreeNode 객체로 만든다.
            cur.left = re_tree(iter_node)    # serialize() 에서 left를 먼저 돌았기에 left를 먼저 연결해 준다.
            cur.right = re_tree(iter_node)    # right()는 left 다음으로 연결하고  다시 재귀호출해서 다음 노드를 가리키낟.
            
            #  재귀가 끝난 경우는 iter_node에 있는 모든 node를 다 돌았단 의미이고 이는 cur이 기존에 
            # TreeNode와 같은 구조로 되어 있다는 의미이다. 따라서, cur 객체를 return 한다.
                
            return cur  

        
        return re_tree(iter_node)   # 완성된 TreeNode 결과가 return 된다. 

        
root = [1,2,3,None, None ,4,5]
res = Codec.serialize(0,root)
res = Codec.deserialize(0,res)




