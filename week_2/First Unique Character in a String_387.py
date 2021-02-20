# leetcode 387 First Unique Character in a String
class Solution:
    def firstUniqChar(self, s: str) -> int:
        result={}
        for ch in s:
            if result.get(ch): # have key
                result[ch]+=1
            else : 
                result[ch]=1
        for r_k, r_v in result.items():
            if r_v == 1:
                return s.index(r_k)
        return -1

s1 = "leetcode"
s2 = "loveleetcode"
res = Solution.firstUniqChar(0,s2)
print(res)