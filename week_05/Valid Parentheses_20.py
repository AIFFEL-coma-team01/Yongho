'''
## 20. 유효한 괄호

'(', ')', '{', '}', '['및 ']'문자 만 포함 된 문자열 s가 주어지면 입력 문자열이 유효한지 확인합니다.

입력 문자열은 다음과 같은 경우에 유효합니다.

열린 브래킷은 동일한 유형의 브래킷으로 닫아야합니다.
1열린 괄호는 올바른 순서로 닫아야합니다.

- 후입선출의 형태로 만들어 본다.
- 왼쪽으로 닫힌 괄호 일때는 입력, 오른쪽으로 닫힌 괄호일 때는 출력의 방식으로 진행하자.


'''

# 32ms
# leetcode 20 : Valid Parentheses
from collections import deque
import re
class Solution:
    def isValid(self, s: str) -> bool:
        queue = deque()
        if len(s)<=1 :  # 문자열 길이가 1일때
            return False
        for ch in s :
            open_bracket = re.search("[\(\{\[]",ch) # 열린 괄호일때 True이다.
            if open_bracket:  # 특정 괄호가 시작 되었으면 
                queue.append(ch) # 열린 괄호 넣기
            else : # 닫힌괄호일 경우
                if len(queue) < 1: # 닫힌괄호가 열린괄호보다 앞에 있는 경우 false이다.
                    return False
                open_ = queue.pop()
                if (open_+ch) == '()' or (open_+ch) == '[]' or (open_+ch) == '{}' :
                    continue
                else :
                    return False
        if len(queue)>0 :  # pop이 안되었다는 의미이니 ( 열린 괄호만 들어간 것이다.
            return False 
        return True