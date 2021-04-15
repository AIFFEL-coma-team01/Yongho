'''
## 242. Valid Anagram
---
두 개의 문자열 s와 t가 주어지면 t가 s의 애너그램[철자바꾸기]이면 true를 반환하고 그렇지 않으면 false를 반환합니다.

4개의 풀이
- 1. sorted 사용 
- 2. merge sort 
- 3. default dict
- 4. Counter

defaultdict와 Counter은 같은 원리로 철자의 개수를 센 후 s,t의 
각 철자마다의 개수가 다른 경우는 애너그램이 아닌 다른 문자열 이므로,
False를 return하게 한다.
'''

## 44ms
# 정렬을 했을때 다른 결과면 다른 철자를 가졌으므로 아래의 코드가 동작할 수 있다.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) ==sorted(t)


## 832ms
# 병합 정렬 사용
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def merge_sort(arr):
            # 병합 정렬 
            if len(arr) < 2: 
                return arr
            
            # 리스트 분할
            half = len(arr)//2
            slow = merge_sort(arr[:half])
            fast = merge_sort(arr[half:])
            
            merged_list = []
            sl = f = 0 
            
            while sl < len(slow) and f < len(fast) : 
                if slow[sl] < fast[f] : 
                    merged_list.append(slow[sl])
                    sl+=1
                else :
                    merged_list.append(fast[f])
                    f +=1
                    
            if sl<len(slow) :
                merged_list.extend(slow[sl:])
            elif f < len(fast): 
                merged_list.extend(fast[f:])
            return merged_list
        

        return merge_sort(s) ==merge_sort(t)


# 아래 코드부턴 collections 모듈의 라이브러리 사용
from collections import defaultdict, Counter

## 56ms
# defaultdict 사용
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t): 
            return False
        dict_s = defaultdict(int)
        dict_t = defaultdict(int)

        def dictCount(_dict, s):
            for ch in s : 
                if _dict[ch] != None :
                    _dict[ch] +=1
            return _dict

        dict_s = dictCount(dict_s, s)
        dict_t = dictCount(dict_t, t)
        
        for ch in s : 
            if dict_s[ch] != dict_t[ch] :
                return False
        
        return True

## 44ms
# Counter 사용
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t): 
            return False
        dict_s = Counter(s)
        dict_t = Counter(t)
        
        for ch in s :
            if dict_s[ch] != dict_t[ch] :
                return False

        
        return True