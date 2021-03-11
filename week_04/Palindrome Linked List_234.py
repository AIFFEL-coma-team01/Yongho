'''
Reverse Linked List

단일 연결 목록이 주어지면 회문인지 확인하십시오.


- deque()로 시자고가 끝이 다른 경우가 있으면 False를 return하게 만들었다.

'''
# 32 ms
# leetcode 234 : Palindrome Linked List

from collections import deque
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        res = deque()
        if not head : 
            return True
        
        while node is not None :
            res.append(node.val)
            head = head.next
            
        while len(res) > 1 :
            if res.popleft(0) != res.pop() : # res에 시작과 끝이 다른 경우
                return False
        
        return True
