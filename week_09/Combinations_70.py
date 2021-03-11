
'''
### 77. Combinations
---

두 개의 정수 n과 k가 주어지면 1 ... n 중에서 k 숫자의 가능한 모든 조합을 반환합니다.

어떤 순서로든 결과를 반환 할 수 있습니다.

## 
조합을 받을 변수 elements에 길이가 k개가 되는 경우 return 시켜주고
 1부터 n 까지이니 총 반복을 n 까지 하게 만듭니다.
'''

# 480ms
class Solution:
    def combine(self, num: int, k: int) -> [[int]]:    
        result, elements = [],[]
        def dfs(n):
            if len(elements) == k : 
                return result.append(elements[:])

            for i in range(n+1, num+1) :
                elements.append(i)
                dfs(i)
                elements.pop()
        dfs(0)
        return result