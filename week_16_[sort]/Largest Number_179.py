'''
## 179. Largest Number
---
음이 아닌 정수 숫자 목록이 주어지면 가장 큰 숫자를 형성하도록 배열하십시오.   
참고 : 결과가 매우 클 수 있으므로 정수 대신 문자열을 반환해야합니다.
'''


# merge sort를 활용해서 [ str(x)+str(y) > str(y)+str(x) ]룰 조건으로
# 정렬을 한다.
# 44ms
class Solution:

    def largestNumber(self, nums: [int]) -> str:
        def largeNum( x, y ):    # largeNum 구별하는 함수
            return str(x)+str(y) > str(y)+str(x)
        
        def mergeSort(nums) :  # nums의 반을 기준으로 슬라이싱 해준다.
            if len(nums) < 2 : 
                return nums
            half = len(nums) // 2
            low  = mergeSort(nums[:half])
            high  = mergeSort(nums[half:])
            
            return merge(low,high)

        def merge(low, high) :  # mergeSort에서 리스트를 분할 했으니 합치면 된다.
            nums = []  # 결과를 보관할 리스트
            l = h = 0

            while l < len(low)  and h < len(high) :   #  len() 보다 짧은 경우에만 실행
                # 클 수록 리스트 앞 쪽에 쌓인다.
                if largeNum(low[l], high[h]) :  # low 가 더 큰 경우 True
                    nums.append(low[l])
                    l+=1
                else :
                    nums.append(high[h])
                    h+=1
            # 남아있는 값들을 각 인덱스를 기준으로  extend 해서 합쳐준다.
            # [], [1] 형태 등
            if l < len(low) :  
                nums.extend(low[l:])

            if h < len(high) :
                nums.extend(high[h:])

            return nums

        result = mergeSort( nums )
        return str(int("".join(map(str,result)))) 




# cmp_tokey를 활용해 sorted를 조정
# -1 인 경우 뒤로, 1인 경우 앞으로, 0인 경우 그대로
# x+y > y+ x ->   x:20, y =3
# 203 > 320  => False
# 아래에 코드엔 1이 리턴 된다.
# 1인 경우 앞으로, 0인 경우 그대로, -1인 경우 뒤로
# 36ms

from functools import cmp_to_key
class Solution:
    @staticmethod
    def cmp(x: str, other: str):

        if x + other < other + x:  # x + y가 큰 경우, 즉 x가 더 큰 경우  ex) 3,20 -> 320, 203
            return 1       # x의 index를 앞으로 옮겨준다. 
        elif x + other == other + x:  # 같은 경우 그대로로 위치해준다. 
            return 0
        else:            # other(y)가 더 큰 경우 뒤로 보내준다.
            return -1

    def largestNumber(self, nums: [int]) -> str:
        if not any(nums):
            return '0'

        return ''.join(sorted(map(str, nums), key = cmp_to_key(self.cmp)))
        
        