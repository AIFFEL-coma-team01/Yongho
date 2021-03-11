'''
### 46. Permutations
---
고유 한 정수의 배열 번호가 주어지면 가능한 모든 순열을 반환합니다. 어떤 순서로든 답변을 반환 할 수 있습니다.

ex)
nums = [1, 2, 3]

nums[0], nums[1] = nums[1], nums[0]
nums
[2, 1, 3]

nums[0], nums[2] = nums[2], nums[0]
nums
[3, 1, 2]

위와 같이 swap을 함으로써 0번 인덱스의 모든 경우를 참조할 수 있습니다. 
그 후 nums[1]이 되면 0번 위치가 아닌 다음 인덱스 위치의 모든 경우를 참조하게 됩니다. 
결과적으로 가장 마지막 인덱스는 swap을 할 필요가 없으니 Permutation을 구할 수 있게됩니다.
'''

# 32 ms
class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        result, elements = [], []
        end = len(nums)-1
        def dfs(n) : # Back-tracking
            if n == end :
                return result.append(nums.copy())

            for i in range(n, end+1) : # end 까지 반복
                nums[n], nums[i] = nums[i], nums[n]  # i번째 노드를 완성시킨다.
                dfs(n+1)
                nums[n], nums[i] = nums[i], nums[n]  # i의 다음 노드를 swap 해준다.        

        dfs(0)
        return  result