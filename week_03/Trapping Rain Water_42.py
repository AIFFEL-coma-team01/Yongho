'''
42. Trapping Rain Water [빗물 트래핑]
각 막대의 너비가 1 인 고도지도를 나타내는 음이 아닌 정수 n 개가 주어지면 
비가 내린 후 얼마나 많은 물을 가둘 수 있는지 계산합니다.



- 배열에 크기를 블럭의 크기라 생각하고 1 0 1 일때는   
- ■ ■ 크기 1 블럭이 양옆에 있고 중간에는 비어있는 구조이다.  
- 여기서 비어 있는 부분에 물이 차이니 저기서 물은 1만큼 가둬집니다.



풀이 :

가장 큰 값을 기준으로 왼쪽에서 오른쪽, 오른쪽에서 왼쪽으로 진행하자.
L : 가장 큰 값을 기준으로 왼쪽에서 오른쪽 증가 값  
R : 가장 큰 값을 기준으로 오른쪽에서 왼족 증가 값
'''

# 44ms
# leetcode 42 : Trapping Rain Wate
class Solution:
    def trap(self, height: [int]) -> int:
        L_p=R_p=0   #왼쪽 포인트, 오른쪽 포인트
        sum_water = 0
        if len(height) >0 :   
            # 리스트가 0이 아닐때 max 연산이 가능하니 해당 부분을 예외처리 한다.
            max_height = height.index(max(height)) 
        else : 
            return 0
 
        # 가장 높은 값을 기준으로 왼-> 우 , 우 -> 왼
        # L
        for h in height[:max_height]:
            if h>= L_p  and h>0:
                L_p = h
            else :
                sum_water += L_p -h

        # R
        for idx , h in enumerate(height[len(height):max_height:-1]) :
            # 끝에서부터 max_hieght 인덱스 전까지
            if h>= R_p  and h>0:
                R_p = h
            else :
                sum_water += R_p -h
        return sum_water

height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
height2 = [2,0,2]
res = Solution.trap(0, height1)
print(res)