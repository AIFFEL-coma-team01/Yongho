
'''
### Top K Frequent Elements
비어 있지 않은 정수 배열이 주어지면 k 개의 가장 빈번한 요소를 반환합니다.

#### note :
- k가 항상 유효하다고 가정 할 수 있습니다. 1 ≤ k ≤ 고유 요소 수입니다.
- 알고리즘의 시간 복잡도는 O (n log n)보다 나아야합니다. 여기서 n은 배열의 크기입니다.
- 답변이 고유하다는 것이 보장됩니다. 즉, 상위 k 개의 빈번한 요소 집합이 고유합니다.
- 어떤 순서로든 답변을 반환 할 수 있습니다.

1. list의 count를 사용해서 빈도수를 센 값과 일반 값을 튜플 형태로 묶는다.

2. 튜플에서 빈도수의 위치가 [1]번이니, sort를 [1] 기준으로 sort하고 내림차순으로 정렬을한다.

3. k의 값만큼 list에서 추출하고 그 값들을 list로 묶는다.
'''



# 1616 ms
# list로 sort 하기
class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        k_dict =[ (n,nums.count(n)) for n in set(nums) ]
        print(k_dict)

        k_dict.sort(key=lambda x:x[1],reverse=True)
        print("sort_k_dict : ", k_dict)

        return [ k_dict[n][0] for n in range(k) ]