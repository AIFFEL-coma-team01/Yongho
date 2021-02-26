'''
## 3. Longest Substring Without Repeating Characters


- 문자열 s가 주어지면 반복되는 문자없이 가장 긴 부분 문자열의 길이를 찾습니다.

반복이 끊어 졌을때 위치를 받아줄 start 변수를 생성한다.
start 변수에서 idx를 빼고 더한 값과 max_len에서의 max 값을 max_len의 저장한다. 

1.  들어온 문자가 이미 저장되있던(문자 중복 )이면서, start가 해당 문자보다 작아야 한다.

 1에서  start <= res[ch] 이 코드는 지금 반복되는 문자를 찾았는데 그 만자가 start보다 뒤에 있다는 의미이다.
 즉, 이미 반복되는 문자가 발생 해서 문자열이 끊겼다는 의미이다.(Substring가 아니게 된다.) 
 따라서 해당 부분을 계산하지 않아도 되니 if의 조건으로 start보다 같거나 클때의 조건을 넣는다.

'''


# 52ms
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, max_len, start = dict(), 0, 0

        for idx, ch in enumerate(s) :
            if res.get(ch) != None and start <= res[ch]:   # 1
                    start = res[ch]+1                       
            max_len = max(max_len, idx-start+1)              
            res[ch]=idx
        return max_len