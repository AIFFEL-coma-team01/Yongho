'''
## 147. Insertion Sort List
---

단일 연결 목록의 머리가 주어지면 삽입 정렬을 사용하여 목록을 정렬하고 정렬 된 목록의 머리를 반환합니다.  

삽입 정렬 알고리즘의 단계 : 

1.  삽입 정렬이 반복되어 반복 할 때마다 하나의 입력 요소를 사용하고 정렬 된 출력 목록을 늘립니다. 

2. 각 반복에서 삽입 정렬은 입력 데이터에서 하나의 요소를 제거하고 정렬 된 목록 내에서 해당 요소가 속한 위치를 찾아 여기에 삽입합니다.     

3. 입력 요소가 남아 있지 않을 때까지 반복됩니다. 

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1948ms 
# 삽입 정렬 사용 
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        root = cur = ListNode()
        while head :   
            # key 값은 2번쨰 자료부터 시작해야하니 cur.next로 있는지 물어본다.
            while cur.next and cur.next.val < head.val : 
         # 뒤에 값이 앞에 값보다 작은 경우 뒤에 값을 앞으로 옮겨 삽입될 위치를 찾는다.
                cur = cur.next  
            
            # 삽입될 위치를 찾았으니 안에 들어있는 값과 위치를 바꾸면서 
            # 연결 리스트를 계속 이어나간다.
            cur.next, head.next ,head = head, cur.next, head.next
            
            
            
            # 다시 시작 부분을 가리켜서 비교를 해나간다.
            cur = root
        return cur.next


# 88ms
# 연결 리스트를 리스트로 
# 리스트를 병합 정렬로 정렬
# 병합 정렬로 정렬한 리스트를 다시 연결리스트로 변환

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # 병합 정렬을 수행할 함수 
        def merge_sort(arr) :
            if len(arr) < 2 :
                return arr

            # 리스트 분할
            half = len(arr) // 2  # 반으로 split
            low_ = merge_sort(arr[:half])
            high_ = merge_sort(arr[half:])

            merged_list =[]
            lo =  hi =0

            # 리스트 병합, 병합할떄 크기를 비교하면서 병합한다.
            while lo < len(low_) and hi < len(high_) :
                if low_[lo] < high_[hi] :
                    merged_list.append(low_[lo])
                    lo+=1
                else :
                    merged_list.append(high_[hi])
                    hi +=1

            # -1로 끝에 부분을 지정할 경우 값이 중복되어서 들어가질 수 있다.
            # 위에서 조건에 맞는 범위를 해야 마지막에 값이 없는 경우와 
            # 값이 1개만 남아있는 경우를 처리할 수 있다.

            print("low : ", low_[lo:])  
            print("high : " ,high_[hi:])
            merged_list.extend(low_[lo:] + high_[hi:]) 
            #merged_list.extend()
            print("lo : ", lo)
            return merged_list
        
        node_list = []
        while head :   # 연결 리스트를 리스트로
            node_list.append(head.val)
            head = head.next
        
        
        node_list = merge_sort(node_list)
        
        # head를 리스트로 변환 했으니 merge_sort를 사용할 수 있다.
        
        root = cur = ListNode()
        for node in sorted(node_list):  # 정렬된 리스트를 다시 연결리스트로
            cur.next = ListNode(node)
            cur = cur.next

        return root.next


# 84ms
# 연결리스트인 상태에서 mergeSort 진행
class Solution:
    def merge_TwoLists(self, l1:ListNode, l2:ListNode) -> ListNode: 
        if l1 and l2: 
            if l1.val > l2.val:  # 작은게 앞으로 가도록
                l1, l2 = l2, l1 
            l1.next = self.merge_TwoLists(l1.next, l2)
        return l1 or l2


    def insertionSortList(self, head: ListNode) -> ListNode:
        if not (head and head.next ):
            return head
        
        # 런너 기법
        half, slow, fast = None, head, head
        while fast and fast.next: 
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None  # half -> slow -> head를 가리키기에 
                          # half.next를 slow가 가리키는 위치를 기점
        
        # split 재귀 호출
        l1 = self.insertionSortList(head)
        l2 = self.insertionSortList(slow)
        
        return self.merge_TwoLists(l1, l2 )


#  결과가 맞게 정렬되었는지 확인하는 부분
head = [4, 2 ,1, 3]
cur = h = ListNode()
for node in head : 
    cur.next = ListNode(node)
    cur = cur.next
res = Solution.insertionSortList(0, h.next)
print(res)

while res :
    print(res.val)
    res = res.next
    