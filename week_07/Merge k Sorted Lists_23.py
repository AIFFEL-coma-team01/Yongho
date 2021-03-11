'''
### k 개의 정렬 된 목록 병합

k 개의 연결된 list 목록이 제공되며 각 연결 목록은 오름차순으로 정렬됩니다.

모든 연결 목록을 하나의 정렬 된 연결 목록으로 병합하고 반환합니다.
'''
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 92ms
# letcod 23 : Merge k Sorted Lists

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        cur = ListNode()  #  merge_list에 1열로 모든 ListNode가 있다.
        merge_list =[]
        merge_sorted_list= cur_merge = ListNode()

        for _list in lists : # lists의 모든 ListNode를 하나씩 부르는 과정
            while _list != None:
                cur.next = _list
                cur = cur.next
                merge_list.append(cur.val)  # 하나씩 들어온 ListNode의 value를 list에 넣어준다,
                _list = _list.next
        merge_list.sort()

        del cur # 용량 확보 , 없어도 됨
        for m_l in merge_list :    # list를 ListNode로 바꿔준다.
            cur_merge.next = ListNode(m_l)
            cur_merge= cur_merge.next
        del cur_merge # 용량 확보, 없어도 됨

        return merge_sorted_list.next