'''
## 973. K Closest Points to Origin
---
points [i] = [xi, yi]가 X-Y 평면의 한 점과 정수 k를 나타내는 점 배열이 주어지면 원점 (0, 0)에 가장 가까운 점 k 개를 반환합니다.
X-Y 평면에서 두 점 사이의 거리는 유클리드 거리 (즉, √ (x1-x2) 2 + (y1-y2) 2)입니다. 어떤 순서로든 답변을 반환 할 수 있습니다. 
답변은 고유 한 것으로 보장됩니다 (순서가있는 경우 제외).

원점에서의 거리니 (0 - x )^2 + ( 0 - y )^2 이다. 
이는 points에 들어온 값 (x,y)일 때 x^2 + y^2 과 같다.
따라서 이 기준을 key로 두고 정렬을 수행하면 오름차순으로 정렬이 되니 작은 값부터 순서대로 정렬이된다.

(작은값) 즉, 원점과 가까운 값을 k개만 return 해야 하니 
슬라이싱으로 k개만 return 시킨다.

'''

# 636ms
class Solution:
    def kClosest(self, points: [[int]], k: int) -> [[int]]:
        res =  sorted(points, key =  (lambda x : (x[0]**2)+(x[1]**2)))
        return res[:k]
        


#  위에 코드를 한줄로 나타낸 것
# 620ms
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key =  (lambda x : (x[0]**2)+(x[1]**2)))[:k]


# 정렬이 어떻게 되었는지 결과 확인 부분
points = [[1,3],[-2,2]]
k = 1

res = Solution.kClosest(0, points,k)
print(res)