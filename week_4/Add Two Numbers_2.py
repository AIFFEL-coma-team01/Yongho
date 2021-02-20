'''
Add Two Numbers

두 개의 음이 아닌 정수를 나타내는 비어 있지 않은 두 개의 연결 목록이 제공됩니다.
숫자는 역순으로 저장되며 각 노드에는 단일 숫자가 포함됩니다.
두 숫자를 더하고 합계를 연결 목록으로 반환합니다.

숫자 0 자체를 제외하고 두 숫자에 선행 0이 포함되어 있지 않다고 가정 할 수 있습니다.



1. 합계를 받을 ListNode를 만들고  그 ListNode를 가리킬 dummy를 만든다.

2. ListNode 1,2의 합을 l3에 저장하는데, 10의 자리 인 경우 %10을 한 몫 을 
   다음 노드에 더하게 만든다.
  
3. dummy에 next를 해서 결과를 return한다.
'''
# 72 ms
# leetcode 2 : Add Two Numbers
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = l3 = ListNode(None)
        decimal =0
        while l1 or l2 or decimal:
            n=0
            if l1:
                n += l1.val
                l1 = l1.next
            if l2 :
                n += l2.val
                l2 = l2.next
            decimal,n = divmod(n+decimal, 10)
            l3.next = ListNode(n)
            l3 = l3.next

        return dummy.next
