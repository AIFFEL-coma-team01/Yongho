'''
### 39. Combination Sum

고유 한 정수 후보 배열과 대상 정수 대상이 주어지면 선택한 숫자가 대상에 합산되는 모든 고유 한 후보 조합 목록을 반환합니다. 
조합은 임의의 순서로 반품 할 수 있습니다. 동일한 수를 후보자 중에서 무제한으로 선택할 수 있습니다. 
선택한 숫자 중 하나 이상의 빈도가 다른 경우 두 조합이 고유합니다. 
목표에 합산되는 고유 조합의 수는 주어진 입력에 대해 150 개 미만의 조합임을 보장합니다.

ex)
입력 :
candidates = [2,3,6,7]
target = 7

----------------------------------------------------------
# 입력이 위와 같을때 i+idx가 없으면, i의 값이 변화가 발생하지 않아 i=0인 채로 dfs를 탐색하게 되고
 i 대신에 idx만 할 경우 같은 원소를 가졌지만 순서만 바뀐 값을 참조하는 경우가 생긴다.
Input : [2,3,5]
          8

Output : [[2,2,2,2],[2,3,3],[3,3,2],[3,5]]  # [2,3,3],[3,3,2]의 원소가 같지만 다른 값으로 출력이 된다. [Permutation]
Expected: [[2,2,2,2],[2,3,3],[3,5]]

----------------------------------------------------------

dfs(target-n, i) 
=>  [[2, 2, 3], [2, 3, 2], [3, 2, 2], [7]]

dfs(target-n, i+idx)  # i를 기준으로 idx를 올려서 참조하게 만든다. # 같은 원소를 가진 경우 참조에서 벗어나게 된다.
=>  [[2, 2, 3], [7]]


1. targetn에 n 값을 빼주고 dfs와 반복을 돌면서 n 값을 계속 리스트로 쌓아간다.
2. target가 0이 되는 경우 결과 리스트에 append 시켜주고 0이 아닌 경우 해당 노드와 연결을 끝낸다.

'''

# 76ms
# leetcode 39  : Combination Sum

class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        result, elements = [], []
        def dfs(target,i):
            if target ==0 : 
                return result.append(elements[:])
            elif target <0 :
                return

            for idx, n in enumerate(candidates[i:]):  # i 가 증가함에 따라 현재 값의 다음 인덱스의 리스트 구조를 가진다.
                elements.append(n)
                dfs(target-n,i+idx) # i+idx를 사용해 같은 경우의 수를 다시 참조하는일이 없도록 한다.
                elements.pop()

        dfs(target,0)
        return result