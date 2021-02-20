# leet_code 125 Valid Palindrome 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s =[ch.lower() for ch in s if ch.isalnum() ]
        return tuple(s) == tuple(reversed(s))

res = Solution.isPalindrome("self","A man, a plan, a canal: Panama")
print(res)