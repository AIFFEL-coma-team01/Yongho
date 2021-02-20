'''
정수 nums의 배열과 정수 대상이 주어지면 대상에 합산되도록 두 숫자의 인덱스를 반환합니다.
각 입력에 정확히 하나의 솔루션이 있다고 가정 할 수 있으며 동일한 요소를 두 번 사용할 수 없습니다.
어떤 순서로든 답변을 반환 할 수 있습니다.

- 동일한 요소를 2번 사용할 수 없고 정확히 하나의 솔루션이 존재한다.
- -> 이 말은 a+b=c가 오로지 하나만 존재한다는 의미이고 이것을 key-value로 보면
- c-b =a , c-a = b target이 되는 c와 둘 중 하나의 값을 빼는 경우  다른 값을 부르게된다.

- Key-Value로 풀자.
'''

class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        res={}
        for i ,n in enumerate(nums):
            Key = target - n
            if res.get(Key) != None:
                return [res[Key],i]
            else :
                res[n] =i

nums1 = [2,7,11,15]
target1 = 9
res = Solution.twoSum(0,nums1, target1)
print(res)