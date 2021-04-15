'''
## 56. Merge Intervals
---
intervals [i] = [start_i, end_i] 인 간격의 배열이 주어지면 모든 겹치는 간격을 병합하고 입력의 모든 간격을 포괄하는 겹치지 않는 간격의 배열을 반환합니다.

key = lambda x : x[0]
- start_i 기준으로 정렬을 합니다. 
  정렬을 할 때  [1,5], [2,3] 과 같이 이미 범위 안에 포함된 인덱스가 있을 수 있으니 
  max()로 끝 부분[1]을 비교해 더 큰 범위가 남아 있게 만듭니다.

'''


#  88ms
class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        intervals = sorted(intervals, key = lambda x : x[0])
        result = []
        #l1, l2 = intervals[:], intervals[1:]
        for i, n in enumerate(intervals) :
            if result and result[-1][1] >= n[0] :
                result[-1][1] = max(result[-1][1],n[1])
            else :
                result.append(n)
        return result