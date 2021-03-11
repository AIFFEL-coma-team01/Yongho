'''
#### 561번 Array Partition I



2n 정수의 정수 배열 num이 주어지면이 정수를 n 쌍 (a1, b1), (a2, b2), ..., (an, bn)으로 
그룹화하여 모든 i에 대한 min (ai, bi)의 합이되도록합니다. 
최대화 된 합계를 반환합니다.

- 작은 순으로 2쌍을 모아서 해당 쌍의 최소를 뽑은 후 다 더한다.
- 2n정수의 정수 배열이니 주어진 리스트의 길이는 짝수 이다.
'''
# 252ms
# leetcode 561 : Array Partition I

# 정렬을 하는 경우 홀수 번째의 값이 무조건 더 작기 때문에
# 해당 값만 따로 뽑아서 리스트를 만든 후 sum을 한다.
# 정렬 후 홀수번째 값만 반복 후 sum하기
class Solution:
    def arrayPairSum(self, nums: [int]) -> int:
        nums.sort() 
        return sum([n for n in nums[0::2]])