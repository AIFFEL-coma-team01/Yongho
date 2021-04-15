'''
### 148. Sort List
--- 
연결 목록의 헤드가 주어지면 오름차순으로 정렬 한 후 목록을 반환합니다. 
후속 조치 : 연결 목록을 O (n logn) 시간과 O (1) 메모리 (즉, 일정한 공간)로 정렬 할 수 있나요?
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 224ms
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        node_list = []
        while head :   # 연결 리스트를 리스트로
            node_list.append(head.val)
            head = head.next
        result = cur = ListNode()
        
        for node in sorted(node_list):  # 정렬된 리스트를 다시 연결리스트로
            cur.next = ListNode(node)
            cur = cur.next
        
        return result.next


# 두 정렬 리스트 병합
# 540ms
def mergeTwoLists(self, l1:ListNode, l2:ListNode) -> ListNode: 
    if l1 and l2: 
        if l1.val > l2.val : # 작은게 앞으로 가도록
            l1, l2 = l2, l1 
        l1.next = self.mergeTwoLists(l1.next, l2)
    return l1 or l2

def sortList(self, head: ListNode) -> ListNode: 
    if not (head and head.next):
        return head
    
    # 런너 기법 활용  :  반을 기준으로 잘라야하기 때문
    half, slow, fast = None, head, head
    while fast and fast.next: 
        half, slow, fast = slow, slow.next, fast.next.next
    half.next = None  # half -> slow -> head를 가리키기에 
                      # half.next를 slow가 가리키는 위치를 기점으로 연결리스트 관계를 끊는다.
    # 분할 재귀 호출
    l1 = self.sortList(head)
    l2 = self.sortList(slow)
    
    return self.mergeTwoLists(l1, l2 )
        