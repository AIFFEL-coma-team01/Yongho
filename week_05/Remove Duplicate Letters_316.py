'''
## Remove Duplicate Letters

모든 문자가 한 번만 나타나도록 중복 문자를 제거하십시오. 
결과가 가능한 모든 결과 중에서 사전 식 순서로 가장 작은 지 확인해야합니다.

'''

# 36ms
# leetcod 316 : Remove Duplicate Letters
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        k = {ch:idx for idx,ch in enumerate(s)}  # 문자열 마지막 인덱스 위치 뽑기
        result = []

        for idx, ch in enumerate(s) :  
            if ch not in result :   # result에 없는 경우 
                    # 1. 크기 비교, 2. 다음 값이 있는지를 두고 resuilt.pop()를 진행한다.
                while result and idx < k[result[-1]] and ch < result[-1]:
                    result.pop()
                result.append(ch)
        return "".join(result)



s1 = "bcabc" # abc
s2 = "cb acdc bc"  # "acdb"
res = Solution.removeDuplicateLetters(0,s2)
print(res)