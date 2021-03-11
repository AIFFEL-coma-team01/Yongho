
'''
### Jewels and Stones ( 보석과 돌 )
당신은 보석 인 돌의 종류를 나타내는 줄 보석과 당신이 가지고있는 돌을 나타내는 돌을받습니다.  
돌의 각 캐릭터는 당신이 가진 돌의 한 종류입니다. 당신은 얼마나 많은 돌이 보석인지 알고 싶습니다.

문자는 대소 문자를 구분하므로 "a"는 "A"와 다른 유형의 돌로 간주됩니다.

- 문자열의 count를 활용하여 문자열 내의 문자 개수 세기

- re 모듈을 활용하여 패턴을 찾고 그 길이를 return 한다.

'''
#  ----- 문자열의 count를 활용한다. -----
# 24ms
# count로 각 원소의 개수를 센 후, sum을 하여 원소의 개수 합을 진행한다.
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum( [stones.count(jewel) for jewel in jewels] )

#  ----- re를 활용해서 풀었던 방법 -----
# 32ms
# jewels를 패턴으로 지정하고 []를 감싸서 각 문자 1개씩으로 지정했다.
# findall을 통해 stones에서 해당 패턴을 가진 문자열을 찾은 후 그 길이를 반환한다.
import re 
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return len(re.findall('['+jewels+']', stones))