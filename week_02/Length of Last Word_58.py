# 28ms
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])


s = "Hello World"  # 5
res = Solution.lengthOfLastWord(0,"Hello World") # 5
print(res)