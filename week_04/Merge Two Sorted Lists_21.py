'''
Merge Two Sorted Lists

두 개의 정렬 된 연결 목록을 병합하고 정렬 된 목록으로 반환합니다.  
목록은 처음 두 목록의 노드를 연결하여 만들어야합니다.

- The number of nodes in both lists is in the range [0, 50].

- -100 <= Node.val <= 100

- Both l1 and l2 are sorted in non-decreasing order.
  - l1과 l2는 모두 감소하지 않는 순서로 정렬됩니다.
'''
# 32 ms
# leetcode 21 :Merge Two Sorted Lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 28 ms,
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #  dummy_head는 l3를 가리키고 있는 부분
    # cur l1,l2중 더 작은 값을 가리키는 cursor 이다. 
        dummy_head = cur = ListNode()
        while l1 != None and l2 != None :
            if  l1.val < l2.val :  # ㅣ_1의 값이 작거나 같은 경우 값을 l_3에 넣어주고 다음 노드를 가리킨다.
                cur.next = l1
                l1 = l1.next
            else :  # ㅣ_2의 값이 작거나 같은 경우 값을 l_3에 넣어주고 다음 노드를 가리킨다.
                cur.next = l2
                l2= l2.next
            cur = cur.next
        cur.next =  l1 or l2
        return dummy_head.next
