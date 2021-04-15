'''
### 215. Kth Largest Element in an Array
---
정수 배열 nums와 정수 k가 주어지면 배열에서 k 번째로 큰 요소를 반환합니다. 정렬 된 순서에서 k 번째 고유 요소가 아니라 k 번째로 큰 요소입니다.


'''

import heapq

# 68ms
# 최대 힙 사용
class Solution:
    def findKthLargest(self, nums: [int], k: int) -> int:
        heap = [[-1*n,n ]for n in nums ]
        heapq.heapify(heap)
        
        while k>0 : 
            res = heapq.heappop(heap)
            print(res)
            k-=1
        return res[1]

# 64ms
# 최소힙을 사용한다.
# 위의 리스트에서 k번째로 큰 요소의 의미는 바꿔 보면
# 전체 리스트 길이에서 k번째 요소 전까지의 모든 요소를 다 최소힙으로 빼면
# 그 다음 요소는 k번째로 큰 요소가 된다.

'''
즉, [1,3,6,2,5]에서  2번째로 큰 요소는 5이다
전체 길이가 5이므로 3번 리스트에서 작은 값을 빼고난 후의 값이 k번째의 값이다. 
전체에서 k번째 크다 -> 전체에서 (전체 -k)+1번째 작다
len(nums)-k+1 = 4  (실제 인덱스로 보면 +1을 더하지 않아도 된다.)

[1,3, 6, 2, 5] pop -> 1 k=1
pop -> 2  k=2
pop-> 3   k=3
k번째 최소힙을 했을때 결과 :
[5,6]
이제 return pop을 하면 k번째 큰 요소가 된다.

'''
class Solution:
    def findKthLargest(self, nums: [int], k: int) -> int:
        heapq.heapify(nums)
        k =  len(nums)-k
        while k>0 : 
            heapq.heappop(nums)
            k-=1
        return heapq.heappop(nums)


# 56 ms
# heap을 사용하지 않은 경우
class Solution:
    def findKthLargest(self, nums: [int], k: int) -> int:
        return sorted(nums)[-1*k]