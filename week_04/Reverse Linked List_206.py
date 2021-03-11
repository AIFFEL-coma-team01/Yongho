'''
Reverse Linked List
단일 연결 목록을 뒤집습니다.


- node.nex를 이전 pre 리스트로 계속 연결하면서 끝날때까지 반복한다.
- node가 None이 될 때 pre는 뒤집힌 연결 리스트의 첫 번째 노드가 된다.
-  node.next, prev, node = prev, node, node.next로 다중 할당 한다.

while로 반복한다.
'''
# 32 ms
# leetcode 206 : Reverse Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node , prev = head, None
        while node:
            node.next, prev, node = prev, node, node.next

        return prev
