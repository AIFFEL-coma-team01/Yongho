# 36ms
# leetcode Rearrange Words in a Sentence 1451
class Solution:
    def arrangeWords(self, text: str) -> str:
        sort_text = sorted(text.split(' '), key = len) 
        return ' '.join(sort_text).capitalize()

s1 = "Leetcode is cool"
s2 = "Keep calm and code on"
res = Solution.arrangeWords(0,s1)
print(res)