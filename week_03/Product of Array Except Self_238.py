
'''
 238. Product of Array Except Self [자신을 제외한 배열의 곱]
n> 1 인 정수 n 개의 배열 num이 주어지면 output [i]가 nums [i]를 제외한 nums의 모든 요소의 곱과 같도록 배열 출력을 반환합니다.

-- 이 문제는 i번 인덱스를 제외한 나머지 배열의 값을 곱한 후 해당 값을 i번 인덱스의 값으로 반환하는 문제이다.


풀이 : 

- 1. 왼쪽 계산할때는 현재 인덱스-1 까지의 계산을 곱한 값을 리스트에 넣는다.

- 그렇게하면, 해당 리스트에는 0으로 시작해서 현재 인덱스 -1의 값이 리스트에 들어 있다.

- 2. 해당 리스트를 가지고 오른쪽 곱을 시작한다.
- 오른쪽 곱은 -1부터 시작해서 자신의 +1인덱스 까지의 곱을 곱한다.

L 곱
- 0번 인덱스를 1로 주고 시작한다.

- i>0 일때 i-1까지의 곱을 리스트에 먼저 저장한다.

'''

# 224ms
# leetcode 238 :  Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        multi_L= multi_R = 1
        result = [1 for i in nums]  # nums만큼 1의 값이 생성
#        print(result)
        for l_idx, n in enumerate(nums) :
            r_idx = (-1)*l_idx-1 # -1,-2,-3...

            result[l_idx] *= multi_L    # 왼쪽부터 곱의 값이 누적되게 만든다.
            multi_L *= n
#            print("multi_L : ",multi_L)
            result[r_idx] *= multi_R   # 오른쪽부터 곱의 값이 누적되게 만든다.
            multi_R *= nums[r_idx]
            #print("multi_R : ",multi_R)
#        print("result : ", result)

        return result


nums1 = [1,2,3,4]
res = Solution.productExceptSelf(0,nums1)
print(res)