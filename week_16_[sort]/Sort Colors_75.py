'''
## 75. Sort Colors
---
빨강, 흰색 또는 파랑 색의 n 개의 객체가있는 배열 번호가 주어지면 동일한 색상의 객체가 빨강, 흰색 및 파랑 순서의 색상으로 인접하도록 제자리에 정렬합니다. 정수 0, 1, 2를 사용하여 각각 빨간색, 흰색, 파란색을 나타냅니다.


'''

# l부터 r로 움직이면서, 0인 지점은 n0에 2인 지점은 r위치에 넣어주고 
# 넣어준 위치에서 범위를 줄여나간다.
# dutch national flag problem [네덜란드 국기 문제]이다.
# 32 ms
class Solution:
    def sortColors(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r, n0 = 0, len(nums)-1, 0  
        
        while l <= r :
            if nums[l] == 0 :  # 0인 경우 n0을 기록
                nums[l], nums[n0] = nums[n0], nums[l]
                l +=1;  n0 +=1 
            elif nums[l] == 2:  # 2인 경우 , r의 2를 기록
                nums[l], nums[r] = nums[r], nums[l]
                r-=1
            else : 
                l+=1
        
        # print(nums)

# 위의 풀이가 정석적인 풀이라면, 
# [0,1,2 ] 3개의 요소만 주어지고 0->1->2 순서대로 쌓아야 하는 문제로 볼때 
# 0,1,2 각 요소의 개수를 세고 그 순서대로 nums의 내용을 변경할 수도 있다. 

# 0,1,2의 반복이니 각 요소의 개수를 센 후 리스트로 합쳐준다.
# 28 ms
class Solution:
    def sortColors(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n0, n1, n2 =0,0,0
        
        for n in nums: 
            if n  ==0 :
                n0 +=1
            elif n ==1 :
                n1+=1
            else :
                n2+=1
        
        nums[:n0] = [0]*n0   # number of 0 
        nums[n0:] = [1]*n1   # number of 1
        nums[n0+n1:]  = [2]*n2  # number of 2
        # print(nums)

#  nums의 결과가 제대로 정렬이 되었는지 보는 부분
nums = [2,0,2,1,1,0] # [0, 0, 1, 1, 2, 2]
res = Solution.sortColors(0, nums)
print(res)